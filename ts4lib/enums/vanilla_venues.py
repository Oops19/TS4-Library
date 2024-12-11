#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from typing import Dict

import services
import sims4
from ts4lib.utils.singleton import Singleton
from sims4.resources import get_resource_key


class VanillaVenues(metaclass=Singleton):
    _data: Dict[int, str] = {}
    _data_rev: Dict[str, int] = {}

    def __init__(self):
        self._manager = 'venues'
        self.init()

    def init(self):
        instance_manager = services.get_instance_manager(sims4.resources.Types[self._manager.upper()])
        if not VanillaVenues._data and instance_manager:
            for (key, tuning) in instance_manager.types.items():
                VanillaVenues._data.update({key.instance: tuning.__name__})
                VanillaVenues._data_rev.update({tuning.__name__: key.instance})

    @property
    def data(self):
        return VanillaVenues._data.copy()

    def name(self, instance_id: int) -> str:
        return VanillaVenues._data.get(instance_id, '')

    def instance_id(self, name: str) -> int:
        return VanillaVenues._data_rev.get(name, 0)
