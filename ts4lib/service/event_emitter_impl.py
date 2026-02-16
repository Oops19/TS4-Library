#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Callable, List

from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.modinfo import ModInfo
from ts4lib.service.event_emitter import EventEmitter
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'EventEmitterImpl', custom_file_path=None)
log.enable()


class EventEmitterImpl(EventEmitter):

    def __init__(self):
        super().__init__()
        log.debug(f"initialized")

    def process_event(self, evt: CustomEvent, original, _self, *args, **kwargs):
        # original is None for calls via 'ServiceImpl(Service)'
        event_name = f"{evt.value}"
        callbacks: List[Callable] = self._listeners.get(evt, [])
        if original is None:
            log.debug(f"process_event({event_name}; args={args}; kwargs={kwargs}; -> {callbacks}")
        else:
            log.debug(f"process_event({event_name}; ({original}, {_self}); args={args}; kwargs={kwargs}; -> {callbacks}")
        rv = None
        for callback in callbacks:
            try:
                if original is None:
                    callback(*args, **kwargs)
                else:
                    rv = callback(original, _self, *args, **kwargs)
            except Exception as e:
                log.warn(f"Failed processing event: {evt} ({e})")
        return rv
