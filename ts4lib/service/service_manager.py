#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Type, TYPE_CHECKING, Union, Dict

from ts4lib.modinfo import ModInfo

if TYPE_CHECKING:
    from ts4lib.service.service_impl import ServiceImpl

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ServiceManager')
log.enable()


class ServiceManager:

    def __init__(self):
        self._started = False
        self._services: Dict[str, Union[Type, "ServiceImpl"]] = {}
        self._critical_services: Dict[str, Union[Type, "ServiceImpl"]] = {}
        log.debug(f"initialized")

    @property
    def started(self) -> bool:
        log.debug(f"started")
        return self._started

    @started.setter
    def started(self, started: bool):
        if self._started:
            return
        self._started = started

    def register_service(self, service: Union[Type, "ServiceImpl"], is_critical: bool = False):
        log.info(f"register_service(service={service}: {type(service)}, is_critical={is_critical}")
        try:
            service_name = service.get_name()
        except:
            service_name = 'CustomService'
        try:
            srv = {service_name: service}
            if is_critical:
                self._critical_services.update(srv)
            else:
                self._services.update(srv)
        except:
            log.error(f"Failed registering service: {service_name} ({service})")

    def get_services_gen(self):
        yield from self._services.items()

    def get_critical_services_gen(self):
        yield from self._critical_services.items()

    def get_service(self, service_name: str) -> Union[None, Type, "ServiceImpl"]:
        if service_name in self._services:
            return self._services.get(service_name)

        return self._critical_services.get(service_name, None)
