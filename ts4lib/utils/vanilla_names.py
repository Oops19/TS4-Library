#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import re
from typing import Tuple, Any

from ts4lib.custom_enums.custom_regions import CustomRegions
from ts4lib.custom_enums.custom_venues import CustomVenues
from ts4lib.utils.location_ids import LocationIDs
from ts4lib.utils.worlds_and_neighbourhoods import WorldsAndNeighbourhoods
from ts4lib.common_enums.enum_types.common_enum import CommonEnum
from ts4lib.utils.sim_name import SimName

import services
from sims.sim import Sim
from routing import SurfaceType, SurfaceIdentifier
# noinspection PyUnresolvedReferences
from sims4.math import Vector3, Quaternion, Transform, Location

from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils


class VanillaNames:
    """ Class to return 'Foo Bar' for enum <EnumName.FOO_BAR: 1> """

    @staticmethod
    def from_enum(enum: CommonEnum) -> str:
        """ deprecated, to e removed with 0.4.0 """
        return enum.name.title().replace('_', ' ')


    @staticmethod
    def to_enum(enum_class: Any, enum_name: str) -> Any:
        """ deprecated, to e removed with 0.4.0 """
        """ Usages:
        * VanillaNames.to_enum(CustomRegions, 'Career Alien World')
        * VanillaNames.to_enum('ts4lib.common_enums.vanilla_regions.CustomRegions', 'Career Alien World')
        """
        if isinstance(enum_class, str):
            _class, class_name = enum_class.rsplit('.', 1)
            _module = __import__(_class, globals(), locals(), [class_name])
            enum_class = getattr(_module, class_name)
        return enum_class[enum_name.replace(' ', '_').upper()]

    @staticmethod
    def nice_name(name: str) -> str:
        name = re.sub(r'^(?:venue|subVenue|Venue)_', r'', name)  # no easy way to revert this (3x venues)
        name = re.sub(r'^(?:region|career)_', r'', name)  # (2x regions)
        name = re.sub(r'^(?:gameObject|obejct|objcet|object|Object|objectDrink)_', r'', name)  # (6x objects + 170x not replaced) 'bedDoubleCLLeatherAB_01'
        name = re.sub(r'([a-z])([A-Z]*[A-Z][a-z])', r'\g<1>_\g<2>', name)  # 'bed_Double_CLLeatherAB_01'
        name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\g<1>_\g<2>', name)  # 'bed_Double_CL_LeatherAB_01'
        name = re.sub(r'([a-z])([A-Z]+)', r'\g<1>_\g<2>', name)  # 'bed_Double_CL_Leather_AB_01'
        name = f"{name[0].upper()}{name[1:]}"  # 'Bed_Double_CL_Leather_AB_01'
        name = name.replace('_', ' ')  # 'Bed Double CL Leather AB 01'
        return name

    @staticmethod
    def get_sim_name(sim_id: int = None) -> Tuple[int, str]:
        try:
            if sim_id is None:
                sim_id = CommonSimUtils.get_active_sim_id()
            sim_name = SimName.get(sim_id)
        except Exception as e:
            sim_id = -1
            sim_name = f"({e})"
        return sim_id, sim_name

    def get_object_name(self, sim_object_id: int) -> Tuple[int, str, str]:
        """
        return: sim_object_id, sim_object_name, sim_object_nice_name
        """
        manager = services.object_manager()
        game_object = manager.get(sim_object_id)
        sim_object_nice_name = ''
        if isinstance(game_object, Sim):
            _, sim_object_name = self.get_sim_name(sim_object_id)
        else:
            try:
                sim_object_name = game_object.__class__.__name__  # 'object_bedDoubleCLLeatherAB_01'
                sim_object_name = self.nice_name(sim_object_name)  # 'Bed Double CL Leather AB 01'
            except Exception as e:
                sim_object_name = f"({e})"
        return sim_object_id, sim_object_name, sim_object_nice_name

    @staticmethod
    def get_location(sim_object_id: int = None, use_parent_object: bool = True) -> Tuple[bool, Location]:
        """
        Returns the location of the game_object or the parent game_object if it exists.
        Setting use_parent_object=False will return the relative object position if the object has a parent.
        """
        try:
            if sim_object_id is None:
                sim_object_id = CommonSimUtils.get_active_sim_id()
            manager = services.object_manager()
            game_object = manager.get(sim_object_id)
            location = game_object._location

            if use_parent_object:
                parent_object = getattr(location, 'parent', None)
                if parent_object:
                    location = getattr(parent_object, '_location', location)
            success = True
        except:
            zone_id = services.current_zone_id()
            position = Vector3(0, 0, 0)
            orientation = Quaternion(0, 0, 0, 1)
            level = 0
            surface = int(SurfaceType.SURFACETYPE_WORLD)
            _transform = Transform(position, orientation)
            _routing_surface = SurfaceIdentifier(zone_id, level, surface)
            location = Location(_transform, _routing_surface)
            success = False
        return success, location

    def get_position(self, location: Location = None, digits: int = 3) -> Tuple[Vector3, str]:
        """ X/Y/Z """
        try:
            if location is None:
                _, location = self.get_location()
                _, child_location = self.get_location(use_parent_object=False)
            else:
                child_location = None
            transform = location.transform
            position = transform.translation

            if isinstance(child_location, Location) and (child_location != location):
                child_transform = child_location.transform
                child_position = child_transform.translation
                position += child_position

            position_str = f"{position.x:.{digits}f}/{position.y:.{digits}f}/{position.z:.{digits}f}"
        except Exception as e:
            position = Vector3(0, 0, 0)
            position_str = f"({e})"
        return position, position_str

    def get_orientation(self, location: Location = None, digits: int = 3) -> Tuple[Quaternion, str]:
        """ X/Y/Z/W """
        try:
            if location is None:
                _, location = self.get_location()
                _, child_location = self.get_location(use_parent_object=False)
            else:
                child_location = None

            transform = location.transform
            orientation = transform.orientation

            if isinstance(child_location, Location) and (child_location != location):
                child_transform = child_location.transform
                child_orientation = child_transform.orientation
                orientation += child_orientation

            orientation_str = f"{orientation.x:.{digits}f}/{orientation.y:.{digits}f}/{orientation.z:.{digits}f}/{orientation.w:.{digits}f}"
        except Exception as e:
            orientation = Quaternion(0, 0, 0, 1)
            orientation_str = f"({e})"
        return orientation, orientation_str

    @staticmethod
    def get_world_name(world_id: int = None) -> Tuple[int, str]:
        """
        Return the world id and name (e.g. 1902162923, 'Willow Creek' - see worlds_and_neighbourhoods.py)
        """
        try:
            if world_id is None:
                world_id = LocationIDs().get_current_world_id()
            wan = WorldsAndNeighbourhoods()
            world_name, neighbourhood_name = wan.get_world_and_neighbourhood_name(world_id)
        except Exception as e:
            world_id = -1
            world_name = f"({e})"
        return world_id, world_name

    @staticmethod
    def get_neighbourhood_name(world_id: int = None) -> Tuple[int, str]:
        """
        Return the world id and neighbourhood name (e.g. 1902162923, 'Foundry Cove' - see worlds_and_neighbourhoods.py)
        """
        try:
            if world_id is None:
                world_id = LocationIDs().get_current_world_id()
            wan = WorldsAndNeighbourhoods()
            world_name, neighbourhood_name = wan.get_world_and_neighbourhood_name(world_id)
        except Exception as e:
            world_id = -1
            neighbourhood_name = f"({e})"
        return world_id, neighbourhood_name

    def get_region_name(self, region_id: int = None) -> Tuple[int, str]:
        """
        Return the region id and name (e.g. 108705, 'Career Alien World' - see vanilla_regions.py)
        """
        try:
            if region_id is None:
                region_id = LocationIDs.get_current_region_id()
            region_name = CustomRegions(region_id).name
        except Exception as e:
            region_id = -1
            region_name = f"({e})"
        return region_id, region_name

    def get_venue_name(self, venue_id: int = None) -> Tuple[int, str]:
        """
        Return the venue id and name (e.g. 190058, 'Acting Studio' - see vanilla_venues.py)
        """
        try:
            if venue_id is None:
                venue_id = LocationIDs.get_current_venue_id()
            venue_name = CustomVenues(venue_id).name
        except Exception as e:
            venue_id = -1
            venue_name = f"({e})"
        return venue_id, venue_name

    @staticmethod
    def get_zone_name(zone_id: int = None) -> Tuple[int, str]:
        """ TODO: Return zone_name """
        """
        Return the zone id and '' (zone name)
        """
        try:
            if zone_id is None:
                sim_id = CommonSimUtils.get_active_sim_id()
                sim = CommonSimUtils.get_sim_instance(sim_id)
                location = getattr(sim, 'location', None)
                if location:
                    zone_id = getattr(location, 'zone_id', 0)
                else:
                    zone_id = 0
            zone_name = ''
        except Exception as e:
            zone_id = -1
            zone_name = f"({e})"
        return zone_id, zone_name

    def get_block_name(self, sim_object_id, position: Vector3 = None) -> Tuple[int, str]:
        """ TODO: Return block_name based on items """
        """ ... """
        try:
            if position is None:
                position, _ = self.get_position()
            zone_id = LocationIDs.get_current_zone_id()
            manager = services.object_manager()
            game_object = manager.get(sim_object_id)
            level = getattr(game_object, 'level', 0)
            block_id = CommonLocationUtils().get_block_id(zone_id, position, level)
            block_name = ''
            if block_id == 0:
                block_name = 'Outside'
        except Exception as e:
            block_id = -1
            block_name = f"({e})"
        return block_id, block_name
