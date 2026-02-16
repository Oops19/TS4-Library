#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Set, Callable, TYPE_CHECKING

from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.modinfo import ModInfo

from ts4lib.service.event_emitter_registry import EventEmitterRegistry
from ts4lib.utils.resilent_injections.injection_utility import InjectionUtility

if TYPE_CHECKING:
    from ts4lib.service.event_emitter_impl import EventEmitterImpl

from ts4lib.utils.singleton import Singleton

from clock import ServerClock
from sims.sim_info_base_wrapper import SimInfoBaseWrapper

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'CustomInjections')
log.enable()


class CustomInjections(metaclass=Singleton):
    r"""
    To be used for injections which can be used by multiple mods.
    1. Add the public event name to CustomEvent
    2. Add a method for the injection here.
    3. Add both to 'self.injections' as {CustomEvent: Callable}

    When a mod registers an event listener for this event, it will be registered. Otherwise, the original method is not touched at all (no injection).

    Usage:
    class MyNewMod:
        @staticmethod
        @custom_event(CustomEvent.SIM_OUTFIT_CHANGE)
        def on_sim_outfit_change(*args, **kwargs):
            return  # process data

    """

    def __init__(self):
        self.active_injections: Set[CustomEvent] = set()
        self.injections = {
            CustomEvent.GAME_TICK: CustomInjections.register_tick_server_clock,
            CustomEvent.SIM_OUTFIT_CHANGE: CustomInjections.register_outfit_change,
        }

    def register_event(self, evt: CustomEvent, func: Callable):
        log.debug(f"Registering {func}({evt})'")
        if evt in self.injections and evt not in self.active_injections:
            log.debug(f"Injecting ({evt}) ...")
            f = self.injections.get(evt)
            f()
            self.active_injections.add(evt)
        ev: "EventEmitterImpl" = EventEmitterRegistry().event_emitter
        ev.add_listener(evt, func)

    @staticmethod
    def register_tick_server_clock():
        if not InjectionUtility.check_signature(ModInfo.get_identity(), ServerClock, 'tick_server_clock', {'absolute_ticks': (1, None)}):
            log.warn(f"register_tick_server_clock() failed due to bad method signature")
            return

        @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), ServerClock, ServerClock.tick_server_clock.__name__, handle_exceptions=True)
        def inj_tick_server_clock(original, self, *args, **kwargs):
            try:
                ev: "EventEmitterImpl" = EventEmitterRegistry().event_emitter
                rv = ev.process_event(CustomEvent.GAME_TICK, original, self, *args, **kwargs)
            except:
                rv = original(*args, **kwargs)
            return rv

    @staticmethod
    def register_outfit_change():
        if not InjectionUtility.check_signature(ModInfo.get_identity(), SimInfoBaseWrapper, '_set_current_outfit_without_distribution', {'value': (1, None)}):
            log.warn(f"register_outfit_change() failed due to bad method signature")
            return

        @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfoBaseWrapper, SimInfoBaseWrapper._set_current_outfit_without_distribution.__name__, handle_exceptions=False)
        def inj_set_current_outfit_without_distribution(original, self, *args, **kwargs):
            try:
                ev: "EventEmitterImpl" = EventEmitterRegistry().event_emitter
                log.debug(f"inj_set_current_outfit_without_distribution.original = {original}: {type(original)}")
                log.debug(f"inj_set_current_outfit_without_distribution.self = {self}: {type(self)}")
                rv = ev.process_event(CustomEvent.SIM_OUTFIT_CHANGE, original, self, *args, **kwargs)
            except:
                rv = original(*args, **kwargs)
            return rv
