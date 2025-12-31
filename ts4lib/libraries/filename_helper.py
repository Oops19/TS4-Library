#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


import os
import re
from re import RegexFlag

from ts4lib.custom_enums.custom_resource_type import CustomResourceType
from ts4lib.custom_enums.package_resource_file_type import PackageResourceFileType


class FilenameHelper:
    PREFIX = "TS4_"
    NAME = 'UNKNOWN'
    FILETYPE = 'binary'

    def __init__(self, parse_str: str = None, t: int = 0, g: int = 0, i: int = 0, name: str = NAME, filetype: str = FILETYPE):
        self._type = 0
        self._group = 0
        self._instance = 0
        self._type_name = ''
        self._filetype = ''

        if parse_str:
            if self._tgi_from_filename(parse_str):
                return
        self._type = t
        self._group = g
        self._instance = i
        if name == FilenameHelper.NAME and CustomResourceType(t) != CustomResourceType.MISSING_VALUE:
            self._type_name = CustomResourceType(t).name
        else:
            self._type_name = name
        if filetype == FilenameHelper.FILETYPE and PackageResourceFileType.get_file_suffix(t) != PackageResourceFileType.DEFAULT:
            self._filetype = PackageResourceFileType.get_file_suffix(t)
        else:
            self._filetype = filetype

    def update_filetype(self):
        pass

    def _tgi_from_filename(self, filename: str) -> bool:
        r"""
        Match everything between '0-0-0' and 'TS4_1234000-80000000-1234567890abcdef.snippt.xml'
        If a full/partial path is prepended it will be removed.
        :param filename:
        :return:
        """
        if os.sep in filename:
            filename = filename.rpartition(os.sep)[2]
        data = re.match(r"^(?:TS4[^0-9a-fA-F])?([0-9a-fA-F]{1,16})[^0-9a-fA-F]([0-9a-fA-F]{1,16})[^0-9a-fA-F]([0-9a-fA-F]{1,16})([^0-9a-fA-F].*)?$", filename, flags=RegexFlag.IGNORECASE)
        if not data:
            return False
        try:
            t = int(f"0x{data.group(1)}", 16)
            g = int(f"0x{data.group(2)}", 16)
            i = int(f"0x{data.group(3)}", 16)
            if CustomResourceType(t) != CustomResourceType.MISSING_VALUE:
                pr_type = CustomResourceType(t).name
            else:
                pr_type = ''
            name_and_suffix = data.group(4)
            if name_and_suffix is None:
                name = pr_type.upper()
                filetype = pr_type.lower()
            else:
                name_and_suffix = name_and_suffix[1:]
                if "." in name_and_suffix:
                    name, _, filetype = name_and_suffix.rpartition('.')
                else:
                    name = pr_type.upper() if pr_type else FilenameHelper.NAME
                    filetype = name_and_suffix
        except Exception as e:
            return False
        else:
            self._type: int = t
            self._instance: int = i
            self._group: int = g
            self._type_name: str = name
            self._filetype: str = filetype
        return True

    @property
    def is_none(self) -> bool:
        if self._type == self._group == self._instance == 0:
            return True
        return False

    @property
    def tgi(self) -> str:
        return f"{self._tgi()}"

    def _tgi(self, tgi_sep: str = '_') -> str:
        return f"{self._type:08X}{tgi_sep}{self._group:08X}{tgi_sep}{self._instance:016X}"

    def as_filename(self, tgi_sep: str = '_', name_sep: str = '.', prefix: str = PREFIX, suffix: str = None, filename: str = None, filetype: str = None, as_utf8: bool = True) -> str:
        """ Return a full or partial file name
        Optional prefix:
        If prefix is supplied it will be use as prefix (e.g. 'TS4_' - with separator).
        Optional suffix:
        If suffix is supplied it will be used as file name with file type (e.g. '.info.png' - with separator).
        If suffix is None use _filename + ._filetype

        Use `.tgi` to get just a TGI string.
        """
        rv = self._tgi(tgi_sep=tgi_sep)
        rv = f"{prefix}{rv}"
        if filename is None:
            filename = self.filename
        if filetype is None:
            filetype = self.filetype
        if suffix is None:
            rv = f"{rv}{name_sep}{filename}.{filetype}"
        else:
            rv = f"{rv}{suffix}"
        if as_utf8:
            return self.as_utf8_fullwidth(rv)
        return rv

    @property
    def type(self) -> int:
        return self._type

    @property
    def group(self) -> int:
        return self._group

    @property
    def instance(self) -> int:
        return self._instance

    @type.setter
    def type(self, type: int):
        self._type = type

    @group.setter
    def group(self, group: int):
        self._group = group

    @instance.setter
    def instance(self, instance: int):
        self._instance = instance

    @property
    def filename(self) -> str:
        return self._type_name

    @property
    def filetype(self) -> str:
        return self._filetype

    @staticmethod
    def as_utf8_fullwidth(filename: str) -> str:
        """
        Convert characters which might be forbidden in a regular filename to full-width UTF-8 characters.
        This allows saving the file name even with ':' '\' etc. in it.
        The FNV value of 'Author:Xyz' is not the same as 'Author：Xyz' - it might seem that the instance ID is wrong.
        @param filename:
        @return:
        """
        return filename.replace('~', '～') \
            .replace('"', '＂') \
            .replace('#', '＃') \
            .replace('%', '％') \
            .replace('&', '＆') \
            .replace(':', '：') \
            .replace('{', '｛') \
            .replace('}', '｝') \
            .replace('*', '＊') \
            .replace('<', '＜') \
            .replace('>', '＞') \
            .replace('?', '？') \
            .replace('/', '／') \
            .replace('|', '｜') \
            .replace('\\', '＼')

    @staticmethod
    def un_utf8_fullwidth(filename: str) -> str:
        return filename.replace('～', '~') \
            .replace('＂', '"') \
            .replace('＃', '#') \
            .replace('％', '%') \
            .replace('＆', '&') \
            .replace('：', ':') \
            .replace('｛', '{') \
            .replace('｝', '}') \
            .replace('＊', '*') \
            .replace('＜', '<') \
            .replace('＞', '>') \
            .replace('？', '?') \
            .replace('／', '/') \
            .replace('｜', '|') \
            .replace('＼', '\\')

    def __str__(self) -> str:
        return f"{self._type:08X}_{self._group:08X}_{self._instance:016X}"

    def __repr__(self) -> str:
        return f"<TGI: {self._type:08X} {self._group:08X} {self._instance:016X} {self._type_name}>"


if __name__ == '__main__':
    print('TS4_729F6C4F-2-3')
    print(FilenameHelper('TS4_729F6C4F-2-3').as_filename())

    print('\nTS4_729F6C4F-2-3.binary')
    print(FilenameHelper('TS4_729F6C4F-2-3.binary').as_filename())

    print('\nTS4_03B33DDF-2-3.xml')
    print(FilenameHelper('TS4_03B33DDF-2-3.xml').as_filename())

    print('\nTS4_000F6C4F-2-3.xml')
    print(FilenameHelper('TS4_000F6C4F-2-3.xml').as_filename())

    print('\nTS4_1111_222_4444.foo.xml')
    fh = FilenameHelper('TS4_1111_222_4444.foo.xml')
    print(fh.tgi)
    print(fh.filename)
    print(fh.filetype)
    print(fh.as_filename())
