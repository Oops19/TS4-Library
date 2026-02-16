from typing import List, Dict

from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_late_load import S4CLZoneLateLoadEvent
from ts4lib.modinfo import ModInfo
from ts4lib.utils.simple_ui_notification import SimpleUINotification
from ts4lib.utils.singleton import Singleton


from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'InjectionUtility')
log.enable()


class LatePopupWarning(metaclass=Singleton):
    def __init__(self):
        self._mods: Dict[str, List[str]] = {}

    def add_message(self, mod_name: str, message: str):
        messages = self._mods.get(mod_name, [])
        messages.append(message)
        self._mods.update({mod_name: messages})

    def show_popup(self):
        if self._mods:
            SimpleUINotification().show('Injection Errors', f"Mods: `{'´, `'.join(list(self._mods.keys()))}´\nSee log file for details.", urgency=1)
            log.error(f"Broken mods:", throw=False)
            for k, vs in self._mods.items():
                for v in vs:
                    log.warn(f"{k}: {v}")

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity())
    def handle_event(event_data: S4CLZoneLateLoadEvent):
        cls = LatePopupWarning()
        cls.show_popup()
