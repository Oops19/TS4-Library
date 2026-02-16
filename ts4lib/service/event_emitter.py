#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Callable, Dict, List

from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.modinfo import ModInfo
from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'EventEmitter', custom_file_path=None)
log.enable()


class EventEmitter:

    def __init__(self):
        self._listeners: Dict[CustomEvent, List[Callable]] = {}
        log.debug(f"initialized")

    def process_event(self, evt: CustomEvent, original, _self, *args, **kwargs):
        raise NotImplementedError

    def add_listener(self, evt: CustomEvent, callback: Callable):
        _callbacks: List[Callable] = self._listeners.get(evt, [])
        _callbacks.append(callback)
        self._listeners.update({evt: _callbacks})
        log.debug(f"add_listener {self._listeners}")

    def remove_listener(self, evt: CustomEvent, callback: Callable):
        _callbacks: List[Callable] = self._listeners.get(evt, [])
        if callback in _callbacks:
            _callbacks.remove(callback)
        if _callbacks:
            self._listeners.update({evt: _callbacks})
        else:
            del self._listeners[evt]
        log.debug(f"add_listener {self._listeners}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.hh.service.dump', 'Log all registered events and callbacks')
    def _o19_cheat_dump_listeners(self, output: CommonConsoleCommandOutput):
        for k, v in self._listeners.items():
            log.debug(f"{k}: {v}")
        output(f"{self._listeners}")
