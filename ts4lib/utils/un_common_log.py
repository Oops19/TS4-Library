#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import os
import re
import time
import traceback
from typing import List, Iterator, Union, Any, Tuple, Dict

from ts4lib.utils.un_common_messaage_type import UnCommonMessageType
from ts4lib.utils.un_logger import UnLogger


class UnCommonLog:
    """
    Class to support logging with either S4.CL while TS4 is running or to STDOUT when running the code locally.
    Usage:
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path = None)
    main() should `import os; os.environ["log_to_stdout"] = "1"` to use print() instead of an S4.CL log file.
    """

    def __init__(self, mod_identifier: str, log_name: str, custom_file_path: str = None):
        self.log: Union[None, Any] = None  # Union[None, CommonLog]
        self.logger: UnLogger = UnLogger.INVALID
        self._enabled_message_types: Tuple[UnCommonMessageType] = (UnCommonMessageType.ERROR, )

        try:
            from sims4communitylib.utils.common_log_registry import CommonMessageType
            from sims4communitylib.utils.common_log_registry import CommonLogRegistry
            from sims4communitylib.utils.common_log_registry import CommonLog
            self.log = CommonLogRegistry.get().register_log(mod_identifier, log_name, custom_file_path)
            self.log.enable()
            self.enable()
            # self.info("Logging to FILE ...")
            self.logger = UnLogger.COMMON_LOG
        except:  # Exception as e:
            self.logger = UnLogger.PRINT
            self.enable()
            self.info("Logging to STDOUT ...")

    def debug(self, message: str, privacy_filter: bool = False):
        if self.is_enabled(UnCommonMessageType.DEBUG):
            self._log_message(UnCommonMessageType.DEBUG, message)  # , privacy_filter=privacy_filter)

    def info(self, message: str, privacy_filter: bool = False):
        if self.is_enabled(UnCommonMessageType.INFO):
            self._log_message(UnCommonMessageType.INFO, message)  # , privacy_filter=privacy_filter)

    def warn(self, message: str, privacy_filter: bool = False):
        if self.is_enabled(UnCommonMessageType.WARN):
            self._log_message(UnCommonMessageType.WARN, message)  # , privacy_filter=privacy_filter)

    def error(
            self,
            message: str,
            _: Any = None,  # message_type: UnCommonMessageType = UnCommonMessageType.ERROR,
            exception: Exception = None,
            throw: bool = True,
            stack_trace: List[str] = None,
            privacy_filter: bool = False
    ):
        if self.is_enabled(UnCommonMessageType.ERROR):
            self._log_message(UnCommonMessageType.ERROR, message, exception=exception, throw=throw, stack_trace=stack_trace, privacy_filter=privacy_filter)

    def strip_private_data(self, message: str) -> str:
        msg = message
        # TODO self.init() me
        rep: Dict[str, str] = {}

        for env_var in ['TS4_MODS_FOLDER', 'TS4_GAME_FOLDER']:
            if env_var in os.environ:
                if os.name == 'nt':
                    rep.update({re.escape(f"{os.path.dirname(os.environ[env_var])}"): f"%{env_var}%{os.sep}.."})
                else:
                    rep.update({re.escape(f"{os.path.dirname(os.environ[env_var])}"): f"${env_var}{os.sep}.."})
        for env_var in ['USERNAME', 'USERPROFILE', 'PROGRAMFILES', 'PROGRAMFILES(X86)', 'PROGRAMW6432']:
            if env_var in os.environ:
                if env_var == 'USERNAME':
                    rep.update({re.escape(f"{os.sep}{os.environ[env_var]}{os.sep}"): f"{os.sep}%{env_var}%{os.sep}"})
                else:
                    rep.update({re.escape(f"{os.environ[env_var]}"): f"%{env_var}%"})
        for env_var in ['USER', 'HOME']:
            if env_var in os.environ:
                if env_var == 'USER':
                    rep.update({re.escape(f"{os.sep}{os.environ[env_var]}{os.sep}"): f"{os.sep}${env_var}{os.sep}"})
                else:
                    rep.update({re.escape(f"{os.environ[env_var]}{os.sep}"): f"${env_var}"})

        for k, v in rep.items():
            try:
                # msg = msg.replace(k, v)
                # print(f"v='{v}'")
                # print(f"k='{k}'")
                # print(f"msg='{msg}'")
                msg = re.sub(k, v, msg, flags=re.I)
            except:
                pass
        return msg

    def _log_message(self, message_type: UnCommonMessageType, message: str,
                     exception: Exception = None, throw: bool = False, stack_trace: List[str] = None, privacy_filter: bool = False):
        if message_type not in self._enabled_message_types:
            return
        if privacy_filter:
            message = self.strip_private_data(message)

        if self.logger == UnLogger.COMMON_LOG:
            try:
                if message_type == UnCommonMessageType.DEBUG:
                    self.log.debug(message)
                elif message_type == UnCommonMessageType.INFO:
                    self.log.info(message)
                elif message_type == UnCommonMessageType.WARN:
                    self.log.warn(message)
                elif message_type == UnCommonMessageType.ERROR:
                    from sims4communitylib.utils.common_log_registry import CommonMessageType
                    message_type = CommonMessageType.ERROR
                    self.log.error(message, message_type, exception, throw, stack_trace)
            except:
                pass
        elif self.logger == UnLogger.PRINT:
            if not exception:
                exception = ''
            if not stack_trace:
                stack_trace = ''
            message_type_2_name = {1: 'ERROR', 2: 'WARN', 3: 'DEBUG', 4: 'INFO'}
            print(f"{time.strftime('%y-%m-%d %H:%M:%S', time.localtime(time.time()))} {message_type_2_name.get(message_type.value, '?')}\t{message}\t{exception}\t{stack_trace}")
            if throw:
                traceback.format_exc()
        else:
            # self.logger == UnLogger.INVALID:
            pass

    def is_enabled(self, message_type: UnCommonMessageType) -> bool:
        return message_type in self._enabled_message_types

    @property
    def enabled(self) -> bool:
        return any(self._enabled_message_types)

    def enable(
        self,
        message_types: Iterator[UnCommonMessageType] = (
            UnCommonMessageType.ERROR,
            UnCommonMessageType.WARN,
            UnCommonMessageType.DEBUG,
            UnCommonMessageType.INFO
        ),
    ) -> None:
        self._enabled_message_types = message_types or tuple()

    def disable(self) -> None:
        self._enabled_message_types = (UnCommonMessageType.ERROR, )
