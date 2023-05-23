#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import os
import re
from typing import Set

from ts4lib.modinfo import ModInfo
from sims4communitylib.utils.common_log_registry import CommonLog


log: CommonLog = CommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name)  # TODO


class FileUtils:
    """
    Class to switch between full path filenames and relative file names excluding the base folder.
    """
    def __init__(self, base_folder: str):
        self.base_folder = base_folder

    def relative_filename(self, filename: str) -> str:
        return filename.replace(self.base_folder + os.sep, '')

    def absolute_filename(self, filename: str) -> str:
        return os.path.join(self.base_folder, filename)

    def find_files(self, pattern: str = r'^.*\.bin$') -> Set[str]:
        """
        Scan 'base_folder' and all sub folders for '*.bin' files and return them all.
        :param pattern: A regular expression pattern. The expression will be compiled.
        :return: A set with '{filename, filename, ...}'
        """
        filenames: Set[str] = set()
        log.debug(f"find_files('{self.base_folder}', '{pattern}')")  # ,  privacy_filter=True)
        try:
            _pattern = re.compile(pattern)
            if self.base_folder and os.path.exists(self.base_folder):
                for root, dirs, files in os.walk(self.base_folder):
                    for filename in files:
                        if re.match(_pattern, filename):
                            filename_path = str(os.path.join(root, filename))
                            filenames.add(filename_path)
                log.debug(f"Found {len(filenames)} files.")
            else:
                log.error(f"Can't read '{self.base_folder}'.", throw=False)
        except Exception as e:
            log.error(f"Exception '{e}'.", throw=False)
        return filenames
