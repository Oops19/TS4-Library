#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Any, List, Dict
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton


log: CommonLog = CommonLogRegistry.get().register_log(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name)
log.enable()


class PrettyDict(object, metaclass=Singleton):

    @staticmethod
    def write(file_name: str, data: Dict, encoding='UTF-8'):
        """
        No check for ' in keys or values. Elements with ' may lead to corrupt files.
        :param file_name:
        :param data:
        :return:
        """

        _o = '{'
        _c = '}'
        _n = '\n'
        _t = '\t'

        def _write(fp, _data: dict, indent: int = 0):

            def _prepare(parameter: Any) -> Any:
                if isinstance(parameter, str):
                    return f'"{parameter}"'
                elif isinstance(parameter, list):
                    new_list: List[str] = list()
                    for elem in parameter:
                        new_list.append(_prepare(elem))
                    return new_list
                elif isinstance(parameter, int):
                    if parameter < 2 ** 16:
                        return f"{parameter:04X}"
                    elif parameter < 2 ** 32:
                        return f"{parameter:08X}"
                    else:
                        return f"{parameter:016X}"
                else:
                    return parameter

            fp.writelines(f"{_o}{_n}")
            indent += 1
            for k, v in _data.items():
                if isinstance(v, dict):
                    fp.writelines(f"{_t * indent}{_prepare(k)}: ")
                    _write(fp, v, indent)
                else:
                    fp.writelines(f"{_t * indent}{_prepare(k)}: {_prepare(v)},{_n}")
            indent -= 1
            if indent > 0:
                fp.writelines(f"{_t * indent}{_c},{_n}")
            else:
                fp.writelines(f"{_t * indent}{_c}{_n}")

        try:
            with open(file_name, 'wt', encoding=encoding) as fp:
                _write(fp, data)
        except Exception as e:
            log.warn(f"Exception '{e}' while saving 'Dict' as text.")
