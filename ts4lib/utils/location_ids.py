#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import services
from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from ts4lib.utils.singleton import Singleton


class LocationIDs(object, metaclass=Singleton):
    """
    Temporary class until S4.CL offers these 4 methods.

    This class will not be documented. It will be removed in the near future.
    """

    @staticmethod
    def get_current_world_id() -> int:
        return CommonLocationUtils.get_current_world_id()

    @staticmethod
    def get_current_neighbourhood_id() -> int:
        return CommonLocationUtils.get_current_world_id()

    @staticmethod
    def get_current_region_id() -> int:
        region_instance = services.current_region()
        return getattr(region_instance, 'guid64', 0)

    @staticmethod
    def get_current_venue_id() -> int:
        active_venue_tuning = services.get_current_venue()
        return getattr(active_venue_tuning, 'guid64', 0)

    @staticmethod
    def get_current_zone_id() -> int:
        return CommonLocationUtils.get_current_zone_id()
