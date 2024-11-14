#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict, Union, Tuple

from objects.game_object import GameObject
from sims.sim import Sim
from ts4lib.utils.singleton import Singleton


class OpacityStore(metaclass=Singleton):
    def __init__(self):
        self._items: Dict[Union[Sim, GameObject], Tuple[bool, float, float]] = {}  # item: (True, opacity, fade_duration)

    def contains(self, item: Union[Sim, GameObject]) -> bool:
        found, _, _ = self.get_opacity_and_fade_duration(item)
        return found

    def get_opacity(self, item: Union[Sim, GameObject]) -> float:
        _, opacity, _ = self.get_opacity_and_fade_duration(item)
        return opacity

    def get_fade_duration(self, item: Union[Sim, GameObject]) -> float:
        _, _, fade_duration = self.get_opacity_and_fade_duration(item)
        return fade_duration

    def get_opacity_and_fade_duration(self, item: Union[Sim, GameObject]) -> Tuple[bool, float, float]:
        return self._items.get(item, (False, 1.0, 0.0))

    @property
    def store(self) -> Dict[Union[Sim, GameObject], Tuple[float, float, float]]:
        return self._items.copy()

    def add(self, item: Union[Sim, GameObject], opacity: float, fade_duration: float = 2.0):
        self._items.update({item: (True, float(opacity), float(fade_duration))})

    def remove(self, item: Union[Sim, GameObject]):
        try:
            del self._items[item]
        except:
            pass
