#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import os
import re
from typing import Set, Tuple, Union

from ts4lib.modinfo import ModInfo


try:
    from sims4communitylib.utils.common_log_registry import CommonLog
    log: CommonLog = CommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name)  # TODO
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)

class FileUtils:
    """
    Class to switch between full path filenames_set and relative file names excluding the base folder.
    """
    def __init__(self, base_folder: str):
        self.base_folder = base_folder

    def relative_filename(self, filename: str) -> str:
        return filename.replace(self.base_folder + os.sep, '')

    def absolute_filename(self, filename: str) -> str:
        return os.path.join(self.base_folder, filename)

    def find_files(self, pattern: str = r'^.*\.bin$', include_sub_directories: bool = True, joined_or_dir_file_tuple: bool = True) -> Union[Set[str], Set[Tuple[str, str]]]:
        """
        Scan 'base_folder' and all sub folders for '*.bin' files and return them all.
        @param pattern: A regular expression pattern. The expression will be compiled.
        @param include_sub_directories: Scan all subdirectories
        @param joined_or_dir_file_tuple:  True: join dir_name and filename; False: Tuple with dir_name and filename
        @return: A set with '{filename, filename, ...}'
        """
        filenames_set: Set[str] = set()
        filenames_tuple: Set[Tuple[str, str]] = set()
        log.debug(f"find_files('{self.base_folder}', '{pattern}')")  # ,  privacy_filter=True)
        try:
            _pattern = re.compile(pattern)
            if self.base_folder and os.path.exists(self.base_folder):
                for root, dirs, files in os.walk(self.base_folder):
                    if include_sub_directories or (self.base_folder == root):
                        for filename in files:
                            if re.match(_pattern, filename):
                                filename_path = str(os.path.join(root, filename))
                                filenames_set.add(filename_path)
                                filenames_tuple.add((root, filename))
                log.debug(f"Found {len(filenames_set)} files.")
            else:
                log.error(f"Can't read '{self.base_folder}'.", throw=False)
        except Exception as e:
            log.error(f"Exception '{e}'.", throw=False)
        if joined_or_dir_file_tuple:
            return filenames_set
        else:
            return filenames_tuple
