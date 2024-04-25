
#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import services

from server_commands.object_commands import _all_objects_gen

from sims4communitylib.utils.common_type_utils import CommonTypeUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils

from ts4lib.utils.objects.lot_object_definition import LotObjectDefinition
from ts4lib.utils.sims.cache.sim_cache import SimCache
from ts4lib.utils.singleton import Singleton
from ts4lib.modinfo import ModInfo

from sims4communitylib.events.build_buy.events.build_buy_enter import S4CLBuildBuyEnterEvent
from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_early_load import S4CLZoneEarlyLoadEvent
from sims4communitylib.events.zone_spin.events.zone_teardown import S4CLZoneTeardownEvent
from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class LotObjects(object, metaclass=Singleton):
    """
    Access all objects which are available on lot / active zone.
    """

    def __init__(self):
        self.objects = {}  # {obj_id: lot_object_definition, ...}
        self.names = {}  # {'name': (obj_id_1, obj_id2, ...), ...}
        self.block_ids = {}  # {block_id: (obj_id_1, obj_id2, ...), ...}

    def get_objects(self):
        if not self.objects:
            self.refresh_cache()
        return self.objects.copy()

    def get_names(self):
        if not self.objects:
            self.refresh_cache()
        return self.names.copy()

    def get_block_ids(self):
        if not self.objects:
            self.refresh_cache()
        return self.block_ids.copy()

    def purge_cache(self):
        """
        Purge the cache when unloading or entering build-buy
        """
        self.objects = {}
        self.names = {}
        self.block_ids = {}

    def refresh_cache(self):
        self.purge_cache()

        manager = services.object_manager()
        lot_filter = None
        for o in _all_objects_gen(manager, lot_filter):
            obj_id = getattr(o, 'id', None)  # object.id == object.definition.id ?
            obj_guid64 = getattr(o, 'guid64', None)  # object.guid64 == object.definition.tuning_file_id

            if CommonTypeUtils.is_sim_instance(o):
                is_sim = True
                log.debug(f"obj_id={obj_id}, obj_guid64={obj_guid64}")
                sim_id = CommonSimUtils.get_sim_id(o)
                log.debug(f"obj_id={obj_id}, obj_guid64={obj_guid64}, sim_id={sim_id}")
                sc = SimCache()
                obj_name = sc.sim_name(sim_id)
            else:
                is_sim = False
                obj_name: str = o.__class__.__name__

            lod = LotObjectDefinition(o, obj_id, obj_guid64, is_sim, obj_name)

            _obj_ids = self.names.get(obj_name, set())
            _obj_ids.add(obj_id)
            self.names.update({obj_name: _obj_ids})

            try:
                obj: o = manager.get(o.id)
                obj_location = getattr(obj, 'location', None)
                log.debug(f"xxxxxxxxx {obj_location}")
                obj_level = getattr(obj, 'level', None)
                obj_zone_id = getattr(obj_location, 'zone_id', None)
                _obj_transform = getattr(obj_location, 'transform', None)
                obj_position = getattr(_obj_transform, 'translation', None)
                obj_orientation = getattr(_obj_transform, 'orientation', None)
                _obj_routing_surface = getattr(obj_location, 'routing_surface', None)  # location.routing_surface.type
                obj_surface_id = int(getattr(_obj_routing_surface, 'type', None))
                block_id = CommonLocationUtils().get_block_id(obj_zone_id, obj_position, obj_level)

                _obj_ids = self.block_ids.get(block_id, set())
                _obj_ids.add(obj_id)
                self.block_ids.update({block_id: _obj_ids})
                lod = LotObjectDefinition(o, obj_id, obj_guid64, is_sim, obj_name, obj_position, obj_orientation, obj_level, obj_surface_id, block_id)
            except Exception as e:
                log.warn(f"Error '{e}' parsing location for '{o.id}'.")

            self.objects.update({obj_id: lod})

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def handle_event(event_data: S4CLBuildBuyEnterEvent):
        LotObjects().purge_cache()

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def handle_event(event_data: S4CLZoneEarlyLoadEvent):
        LotObjects().purge_cache()

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
    def handle_event(event_data: S4CLZoneTeardownEvent):
        LotObjects().purge_cache()

