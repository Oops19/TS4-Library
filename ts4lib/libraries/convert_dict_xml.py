from collections import defaultdict
from typing import List, Union, Dict
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from ts4lib.utils.singleton import Singleton


class ConvertDictXML(metaclass=Singleton):
    def etree_to_dict(self, t: Element):
        d: Union[Dict, None] = {t.tag: {} if t.attrib else None}
        children: List[Element] = list(t)
        if children:
            dd = defaultdict(list)
            for dc in map(self.etree_to_dict, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
        if t.attrib:
            d[t.tag].update(('@' + k, v) for k, v in t.attrib.items())
        if t.text:
            text = t.text.strip()
            if children or t.attrib:
                if text:
                    d[t.tag]['#text'] = text
            else:
                if not isfunction(t.tag):
                    d[t.tag] = text
                else:
                    d.popitem()
                    d['#comment'] = text
        return d

    @staticmethod
    def dict_to_etree(data: Dict):
        def _to_etree(d: Union[Dict, str, None], root: Element):
            if not d:
                pass
            elif isinstance(d, str):
                root.text = d
            elif isinstance(d, dict):
                for k, v in d.items():
                    assert isinstance(k, str)
                    if k.startswith('#'):
                        assert k == '#text' or k == '#comment' and isinstance(v, str)
                        if k == '#text':
                            root.text = v
                        elif k == '#comment':
                            root.append(ElementTree.Comment(v))
                    elif k.startswith('@'):
                        assert isinstance(v, str)
                        root.set(k[1:], v)
                    elif isinstance(v, list):
                        for e in v:
                            _to_etree(e, ElementTree.SubElement(root, k))
                    else:
                        _to_etree(v, ElementTree.SubElement(root, k))
            else:
                raise TypeError('invalid type: ' + str(type(d)))

        assert isinstance(data, dict) and len(data) == 1
        tag, body = next(iter(data.items()))
        node = ElementTree.Element(tag)
        _to_etree(body, node)
        return ElementTree.tostring(node).decode(encoding="UTF-8")
