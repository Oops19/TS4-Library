#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.modinfo import ModInfo

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.service.custom_event import custom_event

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'Test')
log.enable()


class Test:
    @staticmethod
    @custom_event(CustomEvent.SIM_OUTFIT_CHANGE)
    def on_outfit_change(original, self, *args, **kwargs):
        log.debug(f"on_outfit_change()")
        rv = original(self, *args, **kwargs)
        return rv

    @staticmethod
    @custom_event(CustomEvent.ALL_SIMS_SPAWNED)
    def on_all_sims_spawned(*args, **kwargs):
        log.debug(f"on_all_sims_spawned()")
        return True

    @staticmethod
    @custom_event(CustomEvent.ZONE_CLEANUP_OBJECTS)
    def on_zone_cleanup(*args, **kwargs):
        log.debug(f"on_zone_cleanup()")
        return True
