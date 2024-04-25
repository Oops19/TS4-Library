#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import ast
import gzip
import os.path
import pickle
import re
from typing import Dict

from ts4lib.modinfo import ModInfo
from ts4lib.utils.config.pretty_dict import PrettyDict
from ts4lib.utils.singleton import Singleton


from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()


class DictIO(object, metaclass=Singleton):
    def __int__(self):
        self.pickle_protocol = 4

    def load(self, file_name: str, pickle_zip: bool = False, encoding: str = 'UTF-8') -> Dict:
        log.debug(f"Reading '{file_name}'")
        try:
            if pickle_zip:
                with gzip.open(file_name, mode='rb') as fp:
                    return pickle.load(fp)
            else:
                with open(file_name, 'rt', encoding=encoding) as fp:
                    _data = fp.read()
                    _data = re.sub(r",*$", "", _data)  # Remove trailing ',' if any
                    return ast.literal_eval(_data)
        except Exception as e:
            if not os.path.exists(file_name):
                log.warn(f"File '{file_name}' doesn't exist. Creating empty default.")
                default_data = {'': {'': None}}
                self.save(file_name, default_data, pickle_zip=pickle_zip, encoding=encoding)

            else:
                log.warn(f"File '{file_name}' couldn't be read ({e}).")
        return {}

    def save(self, file_name: str, data: Dict, pickle_zip: bool = False, pretty: bool = False, encoding: str = 'UTF-8'):
        """
        Set pickle_zip=True to write as compressed binary format.
        Set pretty=True to write the data properly formatted (human-readable).
        The default is to write the data as-is without formatting but still readable.
        As one file_name can be supplied use two calls to write as ZIP and PRETTY.
        """
        try:
            if pickle_zip:
                with gzip.open(file_name, mode='wb') as fp:
                    pickle.dump(data, fp, protocol=self.pickle_protocol)
            else:
                if pretty:
                    PrettyDict().write(file_name, data, encoding=encoding)
                else:
                    with open(file_name, 'wt', encoding=encoding) as fp:
                        fp.write(f"{data}")
        except Exception as e:
            log.warn(f"File '{file_name}' couldn't be written ({e})!")
