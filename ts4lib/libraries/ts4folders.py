#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import os
import sys
from typing import Union, Tuple

from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton

try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)  # TODO
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)


mod_name = ModInfo.get_identity().name
log.enable()


class TS4Folders:
    """
    Class to detect the Game and Mods folder. It supports the environment variables 'TS4_MODS_FOLDER' and 'TS4_GAME_FOLDER' to set the folder.
    Both the 'Mods' and the 'Game' folder are usually located in a (at least for 'Mods' localized) 'The Sims 4' folder.
    The 'The Sims 4' folder containing 'Mods' will also contain 'mod_logs' (rw), 'mod_data' (rw), GameVersion.txt (ro), lastUIException.txt (ro), ...
    The 'The Sims 4' folder containing 'Game' will also contain the DLCs (ro).
    ro/rw = read only / read write from a perspective of script mods.
    Init with `TS4Folders(ModInfo.get_identity().base_namespace)`
    """

    def __init__(self, namespace: str):
        ts4f = _TS4Folders()
        self._data_folder, self._mods_folder, self._game_folder = ts4f.get_folders(namespace)
        self._config_folder = os.path.join(self._data_folder, 'cfg')

    @property
    def ts4_folder_mods(self) -> Union[str, None]:
        """
        :return: The 'The Sims 4' folder which contains mod_logs, mod_data, saves, Tray, Mods, ...
        """
        if self._mods_folder:
            return os.path.dirname(self._mods_folder)   # 'The Sims 4' (usually in HOME)
        else:
            return None

    @property
    def mods_folder(self) -> Union[str, None]:
        """
        :return: The 'The Sims 4/Mods' folder with Package files.
        """
        return self._mods_folder  # 'The Sims 4/Mods'

    @property
    def data_folder(self) -> Union[str, None]:
        """
        :return: The 'The Sims 4/mod_data/{_namespace}' folder to store configuration data.
        """
        return self._data_folder  # 'The Sims 4/mod_data/basename(mod)'

    @property
    def config_folder(self) -> Union[str, None]:
        """
        :return: The 'The Sims 4/mod_data/{_namespace}/cfg' folder to store configuration data.
        """
        return self._config_folder  # 'The Sims 4/mod_data/basename(mod)/cfg'

    @property
    def ts4_folder_game(self):
        """
        :return: The 'The Sims 4' folder which contains 'Game' and other DLC folders with Package files.
        """
        if self._game_folder:
            return os.path.dirname(self._game_folder)  # 'The Sims 4' (usually in program files)
        return None

    @property
    def game_folder(self):
        """
        :return: The 'The Sims 4/Game' folder. It contains INI files etc.
        """
        return self._game_folder  # 'The Sims 4/Game'


class _TS4Folders(object, metaclass=Singleton):

    _initialized = False

    def __init__(self):
        if _TS4Folders._initialized:
            return

        self.env_ts4_mods_folder = 'TS4_MODS_FOLDER'  # re: s#^(.*/Mods)/.*$#$1#g
        self.env_ts4_game_folder = 'TS4_GAME_FOLDER'  # re: s#^(.*/Game)/.*$#$1#g

        self._initialized = False
        self._game_folder = ''
        self._mods_folder = ''
        self._data_folder = ''
        self._config_folder = ''

        if os.name == 'nt':
            __os = "W10/W11"
            __env = "USERPROFILE"
        else:
            # Mac
            __os = "Mac"
            __env = 'HOME'
        log.debug(f"Detected OS: {__os}")

        # noinspection PyBroadException
        try:
            _home = os.environ[__env]
        except:
            log.warn(f"Variable '{__env}' is not set. Consider setting it manually.'")
            _home = "."

        self._mods_folder = self._set_mods_folder(_home)
        log.info(f"Mods folder: '{self._mods_folder}'.")  # , privacy_filter=True  - privacy_filter not supported by S4CL

        self._game_folder = self._set_game_folder(_home)
        if self._game_folder:
            log.info(f"Game folder: '{self._game_folder}'")
        else:
            log.info(f"Game folder: '{self._game_folder}' (For most mods 'None' is fine).")

        _TS4Folders._initialized = True

    # noinspection PyBroadException
    def _set_mods_folder(self, _home) -> str:
        """
        1st Check ENV
        2nd Check current folder for Mods
        3rd Check the default location
        :param _home: The $HOME variable
        :return:
        """
        try:
            __mods_folder = os.environ[self.env_ts4_mods_folder]
            if os.path.exists(__mods_folder):
                return __mods_folder
            else:
                log.warn(f"'{self.env_ts4_mods_folder}' points to '{__mods_folder} which doesn't exist. Please fix this.")
        except:
            log.debug(f"Set '{self.env_ts4_mods_folder}' to define a custom 'The Sims 4/Mods' folder. Restart Origin afterwards.")

        __mods_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)).partition(f"{os.sep}Mods{os.sep}")[0], 'Mods')
        if os.path.exists(__mods_folder):
            return __mods_folder

        __mods_folder = os.path.join(_home, 'Documents', 'Electronic Arts', 'The Sims 4', 'Mods')  # Fails for localized installations
        if os.path.exists(__mods_folder):
            return __mods_folder

        __mods_folder = os.path.dirname(os.path.abspath(__file__))
        log.error(f"Could not locate the 'The Sims 4' folder. Using '{__mods_folder}'.")  # , privacy_filter=True)
        return __mods_folder

    # noinspection PyBroadException
    def _set_game_folder(self, _home) -> Union[None, str]:
        """
        1st Check ENV
        2nd Check location of base.zip
        3rd Check registry
        4th Check the default locations
        :param _home: The $HOME variable
        :return:
        """
        # ENV
        try:
            __game_folder = os.environ[self.env_ts4_game_folder]
            if os.path.exists(__game_folder):
                return __game_folder
            else:
                log.warn(f"'{self.env_ts4_game_folder}' points to '{__game_folder} which doesn't exist. Please fix this.")
        except:
            log.debug(f"Set '{self.env_ts4_game_folder}' to define a custom 'The Sims 4/Game' folder (Along with 'Game' are the folders 'EPnn', 'FP01', 'GPnn', 'SPnn'). Restart Origin afterwards.")

        # Locate 'encodings' in base.zip
        module_name = 'encodings'
        base_zip = os.path.join('Data', 'Simulation', 'Gameplay', 'base.zip')
        module = sys.modules.get(module_name, None)
        if module:
            if hasattr(module, '__file__') and isinstance(module.__file__, str) and base_zip in module.__file__:
                __game_folder = os.path.join(module.__file__.partition(f"{os.sep}Data{os.sep}")[0], 'Game')
                return __game_folder

        # Registry or blind guess
        if os.name == 'nt':
            try:
                # Windows
                import winreg as winreg
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Maxis\\The Sims 4')
                (__game_folder, _) = winreg.QueryValueEx(key, 'Install Dir')
                if os.path.exists(__game_folder):
                    return os.path.join(__game_folder, 'Game')
                else:
                    log.warn(f"'{__game_folder} (winreg) doesn't exist. Trying to locate a different folder.")
            except Exception as e:
                __game_folder = None
                log.info(f"Game folder could not be set ({e}).")

            for program_files in ['ProgramFiles(x86)', 'ProgramFiles', 'ProgramW6432']:
                try:
                    _program_files = os.environ[program_files]
                    __game_folder = os.path.join(_program_files, 'Origin Games', 'The Sims 4', 'Game')
                    if os.path.exists(__game_folder):
                        return __game_folder
                except Exception:
                    pass
        else:
            __game_folder = os.path.join(os.environ['HOME'], 'Applications', 'The Sims 4.app', 'Contents', 'Game')
            if os.path.exists(__game_folder):
                return __game_folder

        return None

    def get_folders(self, namespace) -> Tuple[str, str, str]:
        _data_folder = os.path.join(os.path.dirname(self._mods_folder), 'mod_data', namespace)
        return _data_folder, self._mods_folder, self._game_folder
