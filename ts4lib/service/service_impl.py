#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import TYPE_CHECKING, Union

from ts4lib.modinfo import ModInfo
from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.service.event_emitter_registry import EventEmitterRegistry
if TYPE_CHECKING:
    from ts4lib.service.event_emitter_impl import EventEmitterImpl
    from sims.sim import Sim
    from sims.sim_info import SimInfo
    from sims.sim_info_base_wrapper import SimInfoBaseWrapper

import services
import build_buy
from sims4.service_manager import Service

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ServiceImpl', custom_file_path=None)
log.enable()


class ServiceImpl(Service):

    def __init__(self):
        log.debug(f"initialized")

    @staticmethod
    def get_name() -> str:
        return 'ServiceImpl'

    def _fire_event(self, evt: CustomEvent, *args, **kwargs):
        ev: "EventEmitterImpl" = EventEmitterRegistry().event_emitter
        return ev.process_event(evt, None, None, *args, **kwargs)

    def start(self, *args, **kwargs):
        build_buy.register_build_buy_enter_callback(self.on_build_buy_enter)
        build_buy.register_build_buy_exit_callback(self.on_build_buy_exit)

        # too early
        # self._register_outfit_changed(None)
        # services.sim_spawner_service().register_sim_spawned_callback(self.on_sim_spawned)
        # client = services.client_manager().get_first_client()
        # if client is not None:
        #     client.register_active_sim_changed(self.on_active_sim_change)

        self._fire_event(CustomEvent.GLOBAL_SERVICE_START, *args, **kwargs)  # TODO return ...

    def stop(self, *args, **kwargs):
        build_buy.unregister_build_buy_enter_callback(self.on_build_buy_enter)
        build_buy.unregister_build_buy_exit_callback(self.on_build_buy_exit)
        self._fire_event(CustomEvent.GLOBAL_SERVICE_STOP, *args, **kwargs)

    def on_build_buy_enter(self, *args, **kwargs):
        self._fire_event(CustomEvent.BUILD_BUY_ENTER, *args, **kwargs)

    def on_build_buy_exit(self, *args, **kwargs):
        self._fire_event(CustomEvent.BUILD_BUY_EXIT, *args, **kwargs)

    def on_active_sim_change(self, *args, **kwargs):
        self._fire_event(CustomEvent.ACTIVE_SIM_CHANGED, *args, **kwargs)

    def on_sim_outfit_changed(self, *args, **kwargs):
        self._fire_event(CustomEvent.SIM_OUTFIT_CHANGED, *args, **kwargs)

    def save(self, *args, **kwargs):
        # def save(self, object_list=None, zone_data=None, open_street_data=None, save_slot_data=None):
        self._fire_event(CustomEvent.GAME_SAVE, *args, **kwargs)

    def pre_save(self, *args, **kwargs):
        self._fire_event(CustomEvent.GAME_PRE_SAVE, *args, **kwargs)

    def setup(self, *args, **kwargs):
        # def setup(self, gameplay_zone_data=None, save_slot_data=None):
        self._fire_event(CustomEvent.GAME_SETUP, *args, **kwargs)

    def load(self, *args, **kwargs):
        # def load(self, zone_data=None):
        self._fire_event(CustomEvent.GAME_LOAD, *args, **kwargs)

    def on_zone_load(self, *args, **kwargs):
        # self._register_outfit_changed(None)
        services.sim_spawner_service().register_sim_spawned_callback(self.on_sim_spawned)
        client = services.client_manager().get_first_client()
        if client is not None:
            client.register_active_sim_changed(self.on_active_sim_change)
        self._fire_event(CustomEvent.ZONE_LOAD, *args, **kwargs)

    def on_zone_unload(self, *args, **kwargs):
        services.sim_spawner_service().unregister_sim_spawned_callback(self.on_sim_spawned)
        self._fire_event(CustomEvent.ZONE_UNLOAD, *args, **kwargs)

    def on_sim_spawned(self, *args, **kwargs):
        # sim = args[0]
        # self._register_outfit_changed(sim)
        self._fire_event(CustomEvent.SIM_SPAWNED, *args, **kwargs)

    def on_zone_startup(self, *args, **kwargs):
        self._fire_event(CustomEvent.ZONE_STARTUP, *args, **kwargs)

    def on_cleanup_zone_objects(self, *args, **kwargs):
        # def on_cleanup_zone_objects(self, client):
        self._fire_event(CustomEvent.ZONE_CLEANUP_OBJECTS, *args, **kwargs)

    def on_all_households_and_sim_infos_loaded(self, *args, **kwargs):
        # def on_all_households_and_sim_infos_loaded(self, client):
        self._fire_event(CustomEvent.HOUSEHOLDS_AND_SIMS_LOADED, *args, **kwargs)

    def on_all_sims_spawned(self, *args, **kwargs):
        self._fire_event(CustomEvent.ALL_SIMS_SPAWNED, self, *args, **kwargs)

    def _register_outfit_changed(self, sim: Union["Sim", "SimInfo", "SimInfoBaseWrapper", None]):
        # dead code - registering a listener for each sim might be a bad idea
        def _reg(sim_info: "SimInfo"):
            try:
                sim_info.unregister_for_outfit_changed_callback(self.on_sim_outfit_changed)
                sim_info.register_for_outfit_changed_callback(self.on_sim_outfit_changed)
                log.debug(f"Outfit change listener registered for '{sim_info}'")
            except Exception as e:
                log.warn(f"Could not register {sim}.on_sim_spawned() - '{e}'")
            return

        if sim:
            try:
                from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
                sim_info = CommonSimUtils.get_sim_info(sim)
                _reg(sim_info)
            except Exception as e:
                log.warn(f"Could not get sim_info for sim '{sim}' - '{e}'")
        else:
            try:
                for sim_info in services.sim_info_manager().get_all():
                    _reg(sim_info)
            except Exception as e:
                log.warn(f"Could not iterate over all sims - '{e}'")
        return
