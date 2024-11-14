#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Union

from objects.base_object import BaseObject
from objects.client_object_mixin import ClientObjectMixin
from objects.game_object import GameObject
from objects.object_enums import ResetReason
from sims.sim import Sim

from sims4communitylib.utils.common_injection_utils import CommonInjectionUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.modinfo import ModInfo
from ts4lib.opacity.opacity_store import OpacityStore


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class OpacityManager:
    """
    Handle custom opacity of objects.
    1 is solid, 0.5 is 50% see-through, and 0 is transparent.
    """

    def __init__(self):
        self.os = OpacityStore()

    def fade_to(self, item: Union[Sim, GameObject], opacity: float, fade_duration: float = 2):
        self.os.add(item, opacity, fade_duration)
        item.fade_out()
        if opacity == 1:
            self.os.remove(item)

    def get_opacity(self, item: Union[Sim, GameObject]) -> float:
        return self.os.get_opacity(item)

    def reset_item(self, item: Union[Sim, GameObject]):
        opacity = 1
        fade_duration = 0
        self.fade_to(item, opacity, fade_duration)

    def reset_all_sims(self):
        for item, opacity in self.os.store.items():
            if isinstance(item, Sim):
                self.reset_item(item)

    def reset_all_objects(self):
        for item, opacity in self.os.store.items():
            if isinstance(item, GameObject):
                self.reset_item(item)

    # def fade_opacity(self, opacity:float, duration:float, immediate=False, additional_channels=None):
    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), ClientObjectMixin, ClientObjectMixin.fade_opacity.__name__)
    def o19_fade_opacity(original, self, opacity: float, duration: float, *args, **kwargs):
        found, opacity, fade_duration = OpacityStore().get_opacity_and_fade_duration(self)
        if found:
            log.debug(f"Fading '{self}' to {opacity} in {fade_duration:.2}s")
        original(self, opacity, fade_duration, *args, **kwargs)

    # def reset(self, reset_reason, source=None, cause=None):
    @staticmethod
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), BaseObject, BaseObject.reset.__name__)
    def o19_opacity_hard_reset(original, self, reset_reason: ResetReason = ResetReason.RESET_EXPECTED, source=None, cause=None, *args, **kwargs):
        found, opacity, fade_duration = OpacityStore().get_opacity_and_fade_duration(self)
        if found:
            log.debug(f'hard_reset({self}, {reset_reason}, {source}, {cause})')
            OpacityManager().reset_item(self)
        return original(self, reset_reason, source, cause, *args, **kwargs)
