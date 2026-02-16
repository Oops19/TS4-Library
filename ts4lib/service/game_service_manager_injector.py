#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Type, Union

from ts4lib.modinfo import ModInfo
from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.service.event_emitter_registry import EventEmitterRegistry
from ts4lib.service.service_manager import ServiceManager
from ts4lib.service.service_impl import ServiceImpl

from ts4lib.utils.singleton import Singleton

from game_services import GameServiceManager

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'GameServiceManagerInjector', custom_file_path=None)
log.enable()


class GameServiceManagerInjector(metaclass=Singleton):

    def __init__(self):
        self._service: Union[Type, "ServiceImpl"] = ServiceImpl()
        self._service_manager: "ServiceManager" = ServiceManager()

        self._service_manager.register_service(self._service, is_critical=False)

    @property
    def service(self) -> Union[Type, "ServiceImpl"]:
        return self._service

    @property
    def service_manager(self) -> "ServiceManager":
        return self._service_manager

    def get_services_gen(self):
        return self._service_manager.get_services_gen()

    def get_critical_services_gen(self):
        return self._service_manager.get_critical_services_gen()

    def register_service(self, service, is_critical: bool = False):
        self._service_manager.register_service(service, is_critical)

    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameServiceManager, GameServiceManager.start_services.__name__, handle_exceptions=False)
    def _injected_start_services(original, self, *args, **kwargs):
        log.debug(f"GameServiceManager.start_services()")
        try:
            for key, service in GameServiceManagerInjector().get_critical_services_gen():
                try:
                    self.register_service(service, is_init_critical=True)
                    log.info(f"... Registered critical service: '{key}'")
                except Exception as e:
                    log.error(f"... Failed registering critical service: {key}", exception=e, throw=False)

            for key, service in GameServiceManagerInjector().get_services_gen():
                try:
                    self.register_service(service, is_init_critical=False)
                    log.info(f"... Registered normal service '{key}'")
                except Exception as e:
                    log.error(f"... Failed registering normal service: '{key}'", exception=e, throw=False)

            EventEmitterRegistry().process_event(CustomEvent.GAME_SERVICES_STARTED)  # Event should fire, but this can't be guaranteed

            log.info(f"... Registered all custom services.")
        except Exception as e:
            log.error("... Unexpected error occurred", exception=e, throw=False)

        original(self, *args, **kwargs)
        log.info(f"Registered all default services.")
