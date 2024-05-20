#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#


import random

from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_household_utils import CommonHouseholdUtils
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.modinfo import ModInfo

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommandArgument, CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.utils.interaction.enqueue_interaction import EnqueueInteraction
from ts4lib.utils.objects.lot_object_definition import LotObjectDefinition
from ts4lib.utils.objects.lot_objects import LotObjects
from ts4lib.utils.sims.cache.sim_cache import SimCache
from ts4lib.utils.tuning_helper import TuningHelper

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class TestPose:
    """Simple code snippet to test poses."""

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.ts4l.test_pose', 'Play a pose.',
        command_arguments=(
                CommonConsoleCommandArgument('pose_name', 'string', 'The pose clip name to play.', is_optional=True),
        )
    )
    def o19_ts4l_test_pose(output: CommonConsoleCommandOutput, pose_name: str = 'a_idle_kneel_x'):
        try:
            output(f"test_pose({pose_name})")
            sim = CommonSimUtils.get_active_sim()
            eq = EnqueueInteraction()
            eq.run_pose(sim, pose_name)
            output('ok')
        except Exception as e:
            output(f"Oops: {e}")
            log.error(f"Oops: {e}", throw=True)

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.ts4l.test_interaction', 'Run an interaction.',
        command_arguments=(
                CommonConsoleCommandArgument('interaction_name', 'string', 'The interaction to run.', is_optional=True),
        )
    )
    def o19_ts4l_test_interaction(output: CommonConsoleCommandOutput, interaction_name: str = 'switch_outfit_*'):
        try:
            output(f"test_interaction({interaction_name})")
            th = TuningHelper()
            tuning_ids = th.get_tuning_ids('INTERACTION', [interaction_name, ])
            interaction_id = random.choice(list(tuning_ids))
            output(f"test_interaction({interaction_id})")

            sim = CommonSimUtils.get_active_sim()
            eq = EnqueueInteraction()
            eq.run_interaction(sim, interaction_id=interaction_id)
            output('ok')
        except Exception as e:
            output(f"Oops: {e}")
            log.error(f"Oops: {e}", throw=True)

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.ts4l.test_object_interaction', 'Run an interaction.',
        command_arguments=(
                CommonConsoleCommandArgument('interaction_name', 'string', 'The interaction to run.', is_optional=True),
                CommonConsoleCommandArgument('object_name', 'string', 'The object to use.', is_optional=True),
        )
    )
    def o19_ts4l_test_object_interaction(output: CommonConsoleCommandOutput, interaction_name: str = 'toilet-use-sitting', object_name='toilet'):
        try:
            output(f"test_object_interaction( {interaction_name}, {object_name})")
            th = TuningHelper()
            tuning_ids = th.get_tuning_ids('INTERACTION', [interaction_name, ])
            interaction_id = random.choice(list(tuning_ids))

            lo = LotObjects()
            object_names = lo.get_names()
            # convert everything to lower as 'object_name' is supplied in lower case
            game_object = None
            _object_id = 0
            for _object_name, _object_ids in object_names.items():
                if object_name in _object_name.lower():
                    output(f"{_object_name} {_object_ids}")
                    _object_id = random.choice(list(_object_ids))
                    objects = lo.get_objects()
                    lot_object_definition: LotObjectDefinition = objects.get(_object_id)
                    game_object = lot_object_definition.game_object
                    break
            if game_object is None:
                output('No game_object found')
                return
            output(f"test_object_interaction({interaction_id}, {_object_id})")

            sim = CommonSimUtils.get_active_sim()
            eq = EnqueueInteraction()
            eq.run_interaction(sim, interaction_id=interaction_id, target=game_object)
            output('ok')
        except Exception as e:
            output(f"Oops: {e}")
            log.error(f"Oops: {e}", throw=True)

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.ts4l.test_sim_interaction', 'Run an interaction.',
        command_arguments=(
                CommonConsoleCommandArgument('sim_name', 'string', 'The sim to interact.', is_optional=True),
                CommonConsoleCommandArgument('interaction_name', 'string', 'The interaction to run.', is_optional=True),
        )
    )
    def o19_ts4l_test_sim_interaction(output: CommonConsoleCommandOutput, sim_name: str = None, interaction_name: str = 'socials_Friendly_CrossAge_Interactions_familyKiss_targeted_alwaysOn_CTYAE_to_CTYAE'):
        try:
            output(f"test_sim_interaction({sim_name}, {interaction_name})")
            th = TuningHelper()
            tuning_ids = th.get_tuning_ids('INTERACTION', [interaction_name, ])
            interaction_id = random.choice(list(tuning_ids))

            sim = CommonSimUtils.get_active_sim()
            target_sim = None
            if sim_name:
                sc = SimCache()
                _sim_ids, _, _, _, _ = sc.get_sim_ids_by_sim_name(sim_name)
                if _sim_ids:
                    sim_id = _sim_ids.pop()
                    target_sim = CommonSimUtils.get_sim_instance(sim_id)
            if not target_sim:
                # No name found or given, choose a random TYAE sim in the same household
                sim_id = CommonSimUtils.get_sim_id(sim)
                sim_info = CommonSimUtils.get_sim_info(sim)
                household_id = CommonHouseholdUtils.get_household(sim_info)
                for _sim_info in CommonHouseholdUtils.get_sim_info_of_all_sims_in_household_generator(household_id):
                    _sim_id = CommonSimUtils.get_sim_id(_sim_info)
                    if sim_id == _sim_id:
                        continue
                    if CommonAgeUtils.is_baby_infant_toddler_or_child(_sim_info):
                        continue
                    target_sim = CommonSimUtils.get_sim_instance(_sim_info)
                    break
            if not target_sim:
                output(f"Couldn't find a suitable target sim.")
                return
            output(f"test_sim_interaction({target_sim}, {interaction_id})")

            # Here we very likely need a SuperInteraction with context.sim and maybe some more things
            """
            si_id = 0
            interaction_manager = services.get_instance_manager(ResourceType.INTERACTION)
            si = interaction_manager.get(si_id)
            hsc = HasStatisticComponent()
            cc = ComponentContainer()
            si.context.sim = sim
            sc = SocialGroup(cc, hsc, si=si, target_sim=target_sim)
            sim._social_groups = sc
            target_sim._social_groups = sc
            interaction.social_groups = sc
            """

            eq = EnqueueInteraction()
            eq.run_interaction(sim, interaction_id=interaction_id, target=target_sim)
            output('ok')
        except Exception as e:
            output(f"Oops: {e}")
            log.error(f"Oops: {e}", throw=True)
