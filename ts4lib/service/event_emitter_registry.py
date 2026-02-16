#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import TYPE_CHECKING
from ts4lib.service.event_emitter_impl import EventEmitterImpl

if TYPE_CHECKING:
    from ts4lib.custom_enums.custom_event import CustomEvent

from ts4lib.utils.singleton import Singleton


class EventEmitterRegistry(metaclass=Singleton):
    def __init__(self):
        self._event_emitter: "EventEmitterImpl" = EventEmitterImpl()

    @property
    def event_emitter(self) -> "EventEmitterImpl":
        return self._event_emitter

    def process_event(self, evt: "CustomEvent"):
        self._event_emitter.process_event(evt, None, None)
