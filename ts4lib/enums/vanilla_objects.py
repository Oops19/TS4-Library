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


class VanillaObjects(metaclass=Singleton):
    _data: Dict[int, str] = {}
    _data_rev: Dict[str, int] = {}

    def __init__(self):
        self._manager = 'objects'
        self.init()

    def init(self):
        instance_manager = services.get_instance_manager(sims4.resources.Types[self._manager.upper()])
        if not VanillaObjects._data and instance_manager:
            for (key, tuning) in instance_manager.types.items():
                VanillaObjects._data.update({key.instance: tuning.__name__})
                VanillaObjects._data_rev.update({tuning.__name__: key.instance})

    @property
    def data(self):
        return VanillaObjects._data.copy()

    def name(self, instance_id: int) -> str:
        return VanillaObjects._data.get(instance_id, '')

    def instance_id(self, name: str) -> int:
        return VanillaObjects._data_rev.get(name, 0)
