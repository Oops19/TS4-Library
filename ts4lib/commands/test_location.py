#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#


from ts4lib.modinfo import ModInfo
from ts4lib.utils.objects.lot_objects import LotObjects
from ts4lib.utils.vanilla_names import VanillaNames

# noinspection PyUnresolvedReferences
from sims4.math import Vector3, Quaternion, Transform, Location

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommandArgument, CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()


class TestLocation:

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.ts4l.log_location', 'Log the location of the current sim or object.',
        command_arguments=(
                CommonConsoleCommandArgument('sim_object_id', 'int', 'The id of an object or a sim, if missing the active sim.', is_optional=True, default_value=-1),
        )
    )
    def o19_ts4l_test_location(output: CommonConsoleCommandOutput, sim_object_id: int = -1):

        vn = VanillaNames()
        if sim_object_id == -1:
            sim_object_id, sim_object_name = vn.get_sim_name()
        else:
            _, sim_object_name, _ = vn.get_object_name(sim_object_id)  # sim_object_id, sim_object_name, sim_object_nice_name
        success, location = vn.get_location(sim_object_id)
        position, position_str = vn.get_position(location)
        orientation, orientation_str = vn.get_orientation(location)
        world_id, world_name = vn.get_world_name()
        world_id, neighbourhood_name = vn.get_neighbourhood_name(world_id)
        venue_id, venue_name = vn.get_venue_name()
        region_id, region_name = vn.get_region_name()
        zone_id, zone_name = vn.get_zone_name()
        block_id, block_name = vn.get_block_name(sim_object_id, position)

        output(f"")
        if success is False:
            output(f"! WARNING: Could not get location. The object ID might be wrong.")
        output(f"Sim/Object: '{sim_object_name}' ({sim_object_id}) at '{position_str}' '{orientation_str}'")
        output(f"World: '{world_name}' >> '{neighbourhood_name}' ({world_id})")
        output(f"Region: '{region_name}' ({region_id})")
        output(f"Venue: '{venue_name}' ({venue_id})")
        output(f"Zone: '{zone_name}' ({zone_id})")
        output(f"Block: '{block_name}' ({block_id})")

        if success is False:
            log.info(f"WARNING: Could not get location. Object ID may be wrong.")
        log.info(f"Sim/Object: '{sim_object_name}' ({sim_object_id}) at '{position_str}' '{orientation_str}'")
        log.info(f"World: '{world_name}' >> '{neighbourhood_name}' ({world_id})")
        log.info(f"Venue: '{venue_name}' ({venue_id})")
        log.info(f"Region: '{region_name}' ({region_id})")
        log.info(f"Zone: '{zone_name}' ({zone_id})")
        log.info(f"Block: '{block_name}' ({block_id})")

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.ts4l.log_lot_objects', 'List objects.',
    )
    def o19_ts4l_test_object_interaction(output: CommonConsoleCommandOutput):
        try:
            log.debug(f"LotObjects.o {LotObjects().objects}")
            log.debug(f"LotObjects.n {LotObjects().names}")
            log.debug(f"LotObjects.b {LotObjects().block_ids}")
            output('ok')
        except Exception as e:
            output(f"Oops: {e}")
            log.error(f"Oops: {e}", throw=True)
