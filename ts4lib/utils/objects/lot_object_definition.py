from typing import Any

#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


# noinspection PyUnresolvedReferences
from sims4.math import Vector3, Quaternion, Transform, Location


class LotObjectDefinition:
    """
    Store object definitions.
    It sets many values to sane values instead of None.
    Set `sane_defaults=False` to keep undefined vales as None
    """
    def __init__(
            self,
            game_object: Any,
            obj_id: int = None,
            guid64: int = None,
            is_sim: bool = None,
            obj_name: str = None,
            obj_position: Vector3 = None,
            obj_orientation: Quaternion = None,
            obj_level:int = None,
            obj_surface_id: int = None,
            obj_block_id: int = None,
            sane_defaults: bool = True):

        self.game_object = game_object
        self.obj_id = obj_id
        self.guid64 = guid64
        self.is_sim = is_sim
        self.obj_name = obj_name
        self.obj_position = obj_position
        self.obj_orientation = obj_orientation
        self.obj_level = obj_level
        self.obj_surface_id = obj_surface_id
        self.obj_block_id = obj_block_id
        self.sane_defaults = sane_defaults

        if sane_defaults:
            if obj_id is None:
                self.obj_id = -1
            if guid64 is None:
                self.guid64 = -1
            if obj_name is None:
                self.obj_name = ''
            if is_sim is None:
                self.is_sim = False
            if obj_position is None:
                self.obj_position = Vector3(0, 0, 0)
            if obj_orientation is None:
                self.obj_orientation = Quaternion(0, 0, 0, 1)  # order: xyzw
            if obj_level is None:
                self.obj_level = 0
            if obj_surface_id is None:
                self.obj_surface_id = 0
            if obj_block_id is None:
                self.obj_block_id = 0

    def __repr__(self):
        o = "{"
        c = "}"
        return (f"{o}'obj_id': {self.obj_id:016X}, 'guid64': {self.guid64:016X}, 'is_sim': {self.is_sim}, 'obj_name': '{self.obj_name}', "
                f"'obj_position': {self.obj_position}, 'obj_orientation': {self.obj_orientation}, "
                f"'obj_level': {self.obj_level}, 'obj_surface_id': {self.obj_surface_id}, 'obj_block_id': {self.obj_block_id}, "
                f"'sane_defaults': {self.sane_defaults}{c}")

    def __str__(self):
        return self.__repr__()
