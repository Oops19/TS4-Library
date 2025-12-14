#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


from typing import Any, Union

import routing
import services
from interactions.context import InteractionContext, QueueInsertStrategy, InteractionSource
from interactions.priority import Priority
from objects.game_object import GameObject
from objects.script_object import ScriptObject
from objects.terrain import TerrainPoint, OceanPoint, PoolPoint
from server.pick_info import PickInfo, PickType
from ts4lib.modinfo import ModInfo
from sims.sim import Sim
from sims4.resources import Types as ResourceType
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class EnqueueInteraction:
    def _push_super_affordance(self, sim: Sim, interaction, target: Union[Sim, GameObject, ScriptObject, TerrainPoint, OceanPoint, PoolPoint] = None, context: InteractionContext = None, **kwargs) -> bool:
        """
        Run the SA as soon as possible. Set insert_strategy, priority, must_run_next to avoid this.
        :param sim: The executing sim.
        :param interaction: The executed interaction
        :param target: The target sim or object. Defaults to {sim}
        :param context: The interaction context. In case it is missing it will be created f(sim, interaction_source, priority, client, insert_strategy, must_run_next, pick)
        :param kwargs: see below
        :param _connection: None ?
        :param clip_name: The clip to play, if any.
        :param priority: Priority.Low / High / Critical; Critical clears other items in the queue, even behind this interaction
        :param interaction_source: InteractionSource.SCRIPT / REACTION / AUTONOMY / PIE_MENU
        :param insert_strategy: QueueInsertStrategy.FIRST / NEXT / LAST
        :param must_run_next:
        :param skip_safe_tests:
        :param skip_test_on_execute:
        :param pick:
        :param insert_strategy:

        def __init__(self, sim, source, priority, run_priority=None, client=None, pick=None, insert_strategy=QueueInsertStrategy.LAST, must_run_next=False,
        continuation_id=None, group_id=None, shift_held=False, carry_target=None, create_target_override=None,
        target_sim_id=None, bucket=InteractionBucketType.BASED_ON_SOURCE, visual_continuation_id=None, restored_from_load=False,
        cancel_if_incompatible_in_queue=False, always_check_in_use=False, source_interaction_id=None, source_interaction_sim_id=None,
        preferred_objects=(), preferred_carrying_sim=None, can_derail_if_constraint_invalid=True, continuation_affordance_chain=[], carry_hand=None):
        """
        _connection = kwargs.get('_connection', None)
        clip_name: Union[str, None] = kwargs.get('clip_name', None)
        priority: int = kwargs.get('priority', Priority.High)
        interaction_source: int = kwargs.get('interaction_source', InteractionSource.SCRIPT)
        insert_strategy: int = kwargs.get('insert_strategy', QueueInsertStrategy.FIRST)
        must_run_next: bool = kwargs.get('must_run_next', True)

        skip_safe_tests: bool = kwargs.get('skip_safe_tests', True)
        kwargs.update({'skip_safe_tests': skip_safe_tests})
        skip_test_on_execute: bool = kwargs.get('skip_test_on_execute', True)
        kwargs.update({'skip_test_on_execute': skip_test_on_execute})

        pick: Union[PickInfo, None] = kwargs.get('pick', None)

        # skip_safe_tests = False
        # skip_test_on_execute = False

        log.debug(f"_push_super_affordance(sim={sim}, sa={interaction}, target={target}, context={context}, pose_name={clip_name}, skip_safe_tests={skip_safe_tests}, skip_test_on_execute={skip_test_on_execute}, {kwargs})")
        if target is None:
            target = sim
        if context is None:
            client = kwargs.get('client', services.client_manager().get(_connection))
            context = InteractionContext(sim, interaction_source, priority, client=client, insert_strategy=insert_strategy, must_run_next=must_run_next, pick=pick)
        return sim.push_super_affordance(super_affordance=interaction, target=target, context=context, **kwargs)

    def _deprecated_push_super_affordance(self, sim: Sim, interaction, target: Union[Sim, Any] = None, pose_name: str = None, _connection=None,
                               priority: Priority = Priority.High, interaction_source: InteractionSource = InteractionSource.SCRIPT,
                               insert_strategy: QueueInsertStrategy = QueueInsertStrategy.FIRST, must_run_next: bool = True, **kwargs) -> bool:
        """
        :param sim: The sim
        :param interaction: The interaction
        :param target: The target sim or object. Defaults to 'sim'
        :param pose_name: The pose to play, if any.
        :param _connection: None
        :param priority: Priority.Low / High / Critical
        :param interaction_source: InteractionSource.SCRIPT / REACTION / AUTONOMY / PIE_MENU

        def __init__(self, sim, source, priority, run_priority=None, client=None, pick=None, insert_strategy=QueueInsertStrategy.LAST, must_run_next=False,
        continuation_id=None, group_id=None, shift_held=False, carry_target=None, create_target_override=None,
        target_sim_id=None, bucket=InteractionBucketType.BASED_ON_SOURCE, visual_continuation_id=None, restored_from_load=False,
        cancel_if_incompatible_in_queue=False, always_check_in_use=False, source_interaction_id=None, source_interaction_sim_id=None,
        preferred_objects=(), preferred_carrying_sim=None, can_derail_if_constraint_invalid=True, continuation_affordance_chain=[], carry_hand=None):
        """
        log.debug(f"_push_super_affordance({sim}, {interaction}, {target}, {pose_name}, {kwargs})")
        if target is None:
            target = sim
        client = services.client_manager().get(_connection)
        context = InteractionContext(sim, interaction_source, priority, client=client, insert_strategy=insert_strategy, must_run_next=must_run_next, pick=None)
        return sim.push_super_affordance(super_affordance=interaction, target=target, context=context, pose_name=pose_name, skip_safe_tests=True, skip_test_on_execute=True, **kwargs)

    def run_pose(self, sim: Sim, clip_name: str, target: Union[Sim, Any] = None, **kwargs):
        log.debug(f"run_pose({sim}, {clip_name}, {kwargs})")

        # <I c="TS4LibraryPoseInteraction" i="interaction" m="ts4lib.anim" n="o19:pose_interaction" s="7355957611031270070"><!-- 66159C79445992B6 -->
        interaction_id = 7355957611031270070
        interaction_manager = services.get_instance_manager(ResourceType.INTERACTION)
        interaction = interaction_manager.get(interaction_id)
        return self._push_super_affordance(sim, interaction, target, clip_name=clip_name, **kwargs)

    def run_interaction(self, sim: Sim, interaction_id: int, target: Union[Sim, Any] = None, **kwargs):
        log.debug(f"run_interaction({sim}, {interaction_id}, {target}, {kwargs})")

        interaction_manager = services.get_instance_manager(ResourceType.INTERACTION)
        interaction = interaction_manager.get(interaction_id)
        return self._push_super_affordance(sim, interaction, target=target, **kwargs)

    def run_terrain_interaction(self, sim: Sim, interaction_id: int, interaction_target: TerrainPoint, **kwargs):
        log.debug(f"run_terrain_interaction({sim}, {interaction_id}, {interaction_target}, {kwargs})")

        position = interaction_target.position
        level = interaction_target.level
        interaction_manager = services.get_instance_manager(ResourceType.INTERACTION)
        interaction = interaction_manager.get(interaction_id)
        routing_surface = routing.SurfaceIdentifier(services.current_zone_id(), level, routing.SurfaceType.SURFACETYPE_WORLD)
        pick = PickInfo(pick_type=PickType.PICK_TERRAIN, target=sim, location=position, routing_surface=routing_surface)
        context = InteractionContext(sim, InteractionContext.SOURCE_SCRIPT_WITH_USER_INTENT, Priority.High, pick=pick, group_id=1)

        self._push_super_affordance(sim, interaction, interaction_target, context, **kwargs)
