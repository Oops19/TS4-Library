#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import hashlib
import os
import re
from typing import Tuple, Dict, Union, Set, Any

from ts4lib.libraries.ts4folders import TS4Folders
from ts4lib.modinfo import ModInfo
from ts4lib.utils.config.dict_io import DictIO
from ts4lib.utils.config.store_parsed import StoreParsed
from ts4lib.utils.config.store_raw import StoreRaw


from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class ReaderInterface:
    def __init__(self, base_namespace: str, files: Dict[str, bool], use_cache: bool = True):
        """
        Reads the supplied files and stores the data in @GlobalConfigUserStore and @GlobalConfigParsedStore
        Access the data with e.g. `getattr(GlobalConfigUserStore(), f"{path}_{file}", {}).
        The file encoding must be UTF-8 or ASCII.
        The file format must be '{'author': {'description': definitions: Dict}}
        It will be converted to {'author:description': parsed_definitions: Set}
        Many data types should be suitable for `definitions` and `parsed_definitions`.

        :param base_namespace: Path element within mod_data, usually the mod_name, ModInfo.get_identity().base_namespace
        :param files: A list of files to read which are located in the directory {path}/. - True to use the cache, False to avoid it.
        """
        self.ts4f = TS4Folders(base_namespace)
        self.base_namespace = base_namespace
        self.files = files
        self.use_cache = use_cache
        self.store_raw = StoreRaw()
        self.store_parsed = StoreParsed()
        self.valid_cache_files = set()
        self._force_refresh = False
        self.pickle_protocol = 4  # currently pickle.HIGHEST_PROTOCOL
        self.dio = DictIO()

        self.cfg_dir = 'config'
        self.cache_dir = 'cache'

        os.makedirs(os.path.join(self.ts4f.data_folder, self.cfg_dir), exist_ok=True)
        os.makedirs(os.path.join(self.ts4f.data_folder, self.cache_dir), exist_ok=True)

    def parse_definitions(self, file: str, definitions: Any) -> Any:
        """
        Override this method to parse the definitions.
        :param definitions:
        :return:
        @param file:
        """
        if isinstance(definitions, set) or isinstance(definitions, list) or isinstance(definitions, tuple):
            return set(definitions)
        log.error(f"Can't parse definitions: {type(definitions)} = '{definitions}' with default method.")
        return None

    @staticmethod
    def file_id(type_file_name) -> str:
        return f"{type_file_name.split('.', 1)[0]}"

    def read_files(self):
        sha_file_name = os.path.join(self.ts4f.data_folder, self.cache_dir, 'sha.txt')
        self.valid_cache_files = self._get_valid_cache_files(sha_file_name)

        for file, _ in self.files.items():
            file_id = self.file_id(file)
            # file_id = ConfigType().file_id(file)
            file_name = os.path.join(self.ts4f.data_folder, self.cfg_dir, file)
            log.debug(f"Reading '{file}' as '{file_id}' from '{file_name}'")
            data = self.dio.load(file_name)
            log.debug(f"data = {data}")
            setattr(self.store_raw, file_id, data)

            if file in self.valid_cache_files:
                file_name = os.path.join(self.ts4f.data_folder, self.cache_dir, file)
                parsed_data = self.dio.load(file_name)
            else:
                parsed_data = {}
                for author, descriptions in data.items():  # {'author': {'description': {definitions}}
                    author = self._normalize_string('author', author)
                    for description, definitions in descriptions.items():
                        description = self._normalize_string('description', description)
                        if author == '' and description == '':
                            continue
                        parsed_definitions = self.parse_definitions(file, definitions)
                        parsed_data.update({f"{author}:{description}": parsed_definitions})

            setattr(self.store_parsed, file_id, parsed_data)

    @property
    def force_refresh(self):
        return self._force_refresh

    @force_refresh.setter
    def force_refresh(self, force_refresh):
        self._force_refresh = force_refresh

    @staticmethod
    def _get_sha(file_name) -> Union[None, str]:
        try:
            s256 = hashlib.sha256()
            with open(file_name, 'rb') as fp:
                s256.update(fp.read())
                return s256.hexdigest()
        except:
            return None

    @staticmethod
    def _normalize_string(nfo: str, text: str) -> str:
        new_text = re.sub(r"[^a-zA-Z0-9_-]", '_', text)
        new_text = re.sub(r"__*", '_', new_text)
        new_text = re.sub(r"(^_|_$)", '', new_text)
        if text != new_text:
            log.warn(f"Invalid characters in {nfo}! Renamed '{text}' to '{new_text}'.")
        return new_text

    def _get_valid_cache_files(self, sha_file_name: str) -> Set:
        sha_data = self.dio.load(sha_file_name)
        game_version = 'gameversion.txt'
        files = self.files.copy()
        files.update({game_version: False})
        valid_cache = set()
        sha_updated = False
        for file, use_cache in files.items():
            if file == game_version:
                file_name = os.path.join(self.ts4f.ts4_folder_mods, file)
            else:
                file_name = os.path.join(self.ts4f.data_folder, self.cfg_dir,  file)
            sha_sum = self._get_sha(file_name)
            if use_cache and sha_sum and sha_sum == sha_data.get(file, None):
                valid_cache.add(file)
            else:
                if sha_sum:
                    sha_data.update({file: sha_sum})
                    sha_updated = True
                if file == game_version:
                    # Keep game_version as last item to allow updating of 'sha_data'
                    # Don't use the cache after a game update.
                    valid_cache = set()
        if sha_updated:
            self.dio.save(sha_file_name, sha_data)
        if self.force_refresh:
            self.force_refresh = False
            valid_cache = set()
        return valid_cache
