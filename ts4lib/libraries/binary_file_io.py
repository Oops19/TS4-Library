#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#

import gzip
import os
import pickle
from typing import Any, Union, Dict, Set, List

from ts4lib.modinfo import ModInfo
try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)
log.enable()


class BinaryFileIO:
    def __init__(self, full_filename: str):
        self.db_file = full_filename
        os.makedirs(os.path.dirname(full_filename), exist_ok=True)
        self.PICKLE_PROTOCOL = 4  # currently pickle.HIGHEST_PROTOCOL
        self.MAX_CHUNK_LENGTH = 60_000  # Max. number of entries in each file

    def read_data(self) -> Union[Set, Dict, None]:
        i = 0
        data = dict()
        while True:
            file = f"{self.db_file}.{i}.gz"
            if os.path.exists(file):
                with gzip.open(file, mode='rb') as fp:
                    _data = pickle.load(fp)
                    data.update(_data)
                    i += 1
            else:
                break
        return data

    def write_data(self, data: Union[Set, Dict], print_pretty=False):
        data_length = len(data)
        i = j = 0
        if data_length <= self.MAX_CHUNK_LENGTH:
            file = f"{self.db_file}.{i}.gz"
            with gzip.open(file, mode='wb') as fp:
                pickle.dump(data, fp, protocol=self.PICKLE_PROTOCOL)
        else:
            chunk_size = int(data_length / (1 + int(data_length / self.MAX_CHUNK_LENGTH)))
            _data = dict()
            for k, v in data.items():
                _data.update({k: v})
                j += 1
                if j > chunk_size:
                    file = f"{self.db_file}.{i}.gz"
                    with gzip.open(file, mode='wb') as fp:
                        pickle.dump(_data, fp, protocol=self.PICKLE_PROTOCOL)
                    i += 1
                    j = 0
                    _data = dict()
            file = f"{self.db_file}.{i}.gz"
            with gzip.open(file, mode='wb') as fp:
                pickle.dump(_data, fp, protocol=self.PICKLE_PROTOCOL)

        if print_pretty and isinstance(data, dict):
            self.write_pretty_dict(data)

    def write_pretty_dict(self, data: Dict):
        """
        No check for ' in keys or values. Elements with ' may lead to corrupt files.
        :param filename:
        :param data:
        :return:
        """
        filename = f"{self.db_file}.dict"
        _o = '{'
        _c = '}'
        _n = '\n'
        _t = '\t'

        def _write(fp, _data: Dict, indent: int = 0):

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
                        return f"0x{parameter:04X}"
                    elif parameter < 2 ** 32:
                        return f"0x{parameter:08X}"
                    else:
                        return f"0x{parameter:016X}"
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
            with open(filename, 'wt', encoding='utf-8') as fp:
                _write(fp, data)
        except Exception as e:
            log.warn(f"Exception '{e}' while saving as 'text'.")
