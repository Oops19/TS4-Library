#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


# Original in TS4-Library/ts4lib/libraries/file_utils.py


import os
import re
from typing import Set, Tuple, Union, List

from ts4lib.modinfo import ModInfo
try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
except:
    from ts4lib.utils.un_common_log import UnCommonLog

    log: UnCommonLog = UnCommonLog(ModInfo.get_identity().name, ModInfo.get_identity().name,  custom_file_path=None)
log.enable()


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

    def find_files(self, pattern: str = r'^.*\.bin$', include_sub_directories: bool = True, as_dir_file_tuple: bool = False, exclude: str = None, exclude_dir: str = None, exclude_file: str = None) -> Union[List[str], Set[Tuple[str, str]]]:
        """
        Scan 'base_folder' and all sub folders for '*.bin' files and return them all.
        @param pattern: A regular expression pattern. The expression will be compiled.
        @param include_sub_directories: Scan all subdirectories
        @param as_dir_file_tuple:  True: join dir_name and filename; False: Tuple with dir_name and filename
        @param exclude: Files/directories containing this string will not be returned. If set it is copied to exclude_dir and exclude_file
        @param exclude_dir: Directories containing this string will not be returned.
        @param exclude_file: Files containing this string will not be returned.
        @return: A set with '{filename, filename, ...}'
        """
        filenames_set: Set[str] = set()
        filenames_tuple: Set[Tuple[str, str]] = set()
        if exclude:
            exclude_dir = exclude
            exclude_file = exclude
        log.debug(f"find_files('{self.base_folder}', p='{pattern}', sub_dir='{include_sub_directories}', join='{as_dir_file_tuple}', !dir='{exclude_dir}', !file='{exclude_file}')")  # ,  privacy_filter=True)

        try:
            _pattern = re.compile(pattern)
            if self.base_folder and os.path.exists(self.base_folder):
                for root, dirs, files in os.walk(self.base_folder):
                    if exclude_dir is not None and exclude_dir in root:
                        continue
                    if include_sub_directories or (self.base_folder == root):
                        for filename in files:
                            if exclude_file is not None and exclude_file in filename:
                                continue
                            if re.match(_pattern, filename):
                                filename_path = str(os.path.join(root, filename))
                                filenames_set.add(filename_path)
                                filenames_tuple.add((root, filename))
                log.debug(f"Found {len(filenames_set)} files.")
            else:
                log.warn(f"Can't read '{self.base_folder}'.")
        except Exception as e:
            log.warn(f"Oops '{e}'.")
        if as_dir_file_tuple:
            return filenames_tuple
        else:
            filenames = list(filenames_set)
            filenames.sort()
            return filenames


