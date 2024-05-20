#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


from typing import Union, Tuple, List, Set

import sims4
import sims4.commands
import services
import interactions
from sims4.resources import get_resource_key
from interactions.utils.success_chance import SuccessChance
from interactions.utils.tunable import DoCommand
from interactions import ParticipantType

from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton
from ts4lib.utils.tuning_helper import TuningHelper

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class BasicExtras(metaclass=Singleton):

    def add_do_command(self, manager: str, tunings: Union[List[str], Set[int]], command: Union[str, None], parameter: str, timing: str = 'at_end',
                       offset_time: Union[None, float] = None, xevt_id: Union[None, int] = None,
                       drop_all_basic_extras: bool = False, drop_basic_extras: List[str] = None, include_target_sim: bool = True, ):
        """
        Set command (and parameter) to None to remove only
        :param drop_all_basic_extras: Set to 'True', to remove all 'basic_extras', whatever their content is.
        :param drop_basic_extras: Add classes to drop. E.g.:
            'TunableBuffElementWrapper.factory'
            'TunableStateChangeWrapper._factory'
            'TunableDoCommandWrapper.DoCommand'
            'TunableLootElementWrapper.LootElement'
            'TunablePregnancyElementWrapper.PregnancyElement'
            'TunableTunableAudioStingWrapper.TunableAudioSting'
            'TunableBroadcasterRequestWrapper.BroadcasterRequest'
            'TunableNotificationElementWrapper.NotificationElement'
            'TunablePlayVisualEffectElementWrapper.PlayVisualEffectElement'
        :param include_target_sim: Set to 'False', to have only the actor. Normally the target sim is added as a 3rd parameter.
        """
        parameter = parameter.replace(' ', '').strip()
        log.debug(f"add_do_command({manager}, {tunings}, {command}, {parameter}, {timing}, {offset_time}, {xevt_id}, {drop_all_basic_extras}, {drop_basic_extras}, {include_target_sim}.)")
        if drop_basic_extras is None:
            drop_basic_extras = []
        tuning_dict = TuningHelper().get_tuning_dict(manager, tunings)
        for tuning_id, tuning_data in tuning_dict.items():
            tuning, manager_name, tuning_name = tuning_data
            log.debug(f"Processing '{tuning_name}({tuning_id})'")
            if tuning:
                # basic_extra = self._create_basic_extras(command, f"id({tuning_id})+{parameter}", timing, offset_time, xevt_id, include_target_sim=include_target_sim)
                basic_extra = self._create_basic_extras(command, f"id({tuning_id})+{parameter}", timing, offset_time, xevt_id, include_target_sim=include_target_sim)

                basic_extras: Tuple = (basic_extra,)

                if not drop_all_basic_extras:
                    # Keep some/all existing basic_extras
                    for basic_extra in getattr(tuning, 'basic_extras', []):
                        if f'{basic_extra}' in drop_basic_extras:
                            log.debug(f"Dropping '{basic_extra}'")
                            continue
                        # log.debug(f"Adding basic_extra '{basic_extra}: {type(basic_extra)}'")
                        if command is not None:
                            basic_extras += (basic_extra,)

                setattr(tuning, 'basic_extras', basic_extras)
                log.debug(f"New basic_extras: {getattr(tuning, 'basic_extras', None)}")
            else:
                log.warn(f"Didn't find '{tuning_name}({tuning_id})'")

    # noinspection PyMethodMayBeStatic
    def _create_basic_extras(self, command: str, parameter: str = '', timing: str = 'at_end', offset_time: Union[None, float] = None, xevt_id: Union[None, int] = None, include_target_sim: bool = True):
        """
        :param xevt_id:
        :param command: Create a local `@Command(command, command_type=CommandType.Live)` method
        :param parameter: The 1st argument. The 2nd argument will be 'ParticipantType.Actor'
        :param timing: Set it to 'at_beginning', 'at_end' (default) or 'on_xevt'
        :param offset_time: valid for 'at_beginning', it is recommended to use 'on_xevt' instead.
        :return:
        """
        basic_extras = None
        if timing != 'at_beginning':
            offset_time = None
        try:
            from sims4.tuning.tunable import TunableVariant, TunableReference, TunableList, TunableFactory, TunableTuple, OptionalTunable, TunableSimMinute, TunableRange, Tunable, HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntry, TunableOperator, TunableEnumFlags, HasTunableFactory
            from element_utils import CleanupType
            from sims4.collections import make_immutable_slots_class
            from ui.ui_dialog import CommandArgType
            import collections
            __tuned_values = dict()

            class Slots:
                pass

            __tuned_values.update({'command': command})
            __tuned_values.update({'success_chance': SuccessChance.ONE})  # SuccessChance.ONE = SuccessChance(base_chance=1, multipliers=())

            __arguments_t1 = dict()
            __arguments_t1.update({'arg_type': CommandArgType.ARG_TYPE_STRING})
            __arguments_t1.update({'argument': parameter})
            Slots.__slots__ = 'arg_type', 'argument'
            __arguments_t1_c = make_immutable_slots_class(Slots.__slots__)
            __arguments_t1_is = __arguments_t1_c(__arguments_t1)

            __arguments_t2 = dict()
            __arguments_t2.update({'arg_type': CommandArgType.ARG_TYPE_BOOL})
            __arguments_t2.update({'argument': ParticipantType.Actor})
            Slots.__slots__ = 'arg_type', 'argument'
            __arguments_t2_c = make_immutable_slots_class(Slots.__slots__)
            __arguments_t2_is = __arguments_t2_c(__arguments_t2)

            if include_target_sim:
                __arguments_t3 = dict()
                __arguments_t3.update({'arg_type': CommandArgType.ARG_TYPE_BOOL})
                __arguments_t3.update({'argument': ParticipantType.TargetSim})
                Slots.__slots__ = 'arg_type', 'argument'
                __arguments_t3_c = make_immutable_slots_class(Slots.__slots__)
                __arguments_t3_is = __arguments_t3_c(__arguments_t3)

                __tuned_values.update({'arguments': (__arguments_t1_is, __arguments_t2_is, __arguments_t3_is,)})
            else:
                __tuned_values.update({'arguments': (__arguments_t1_is, __arguments_t2_is,)})

            __timing = dict()
            __timing.update({'criticality': CleanupType.OnCancel})
            if offset_time:
                __timing.update({'offset_time': offset_time})
            else:
                __timing.update({'offset_time': None})
            __timing.update({'supports_failsafe': None})
            __timing.update({'timing': timing})
            __timing.update({'xevt_id': xevt_id})
            Slots.__slots__ = 'criticality', 'offset_time', 'supports_failsafe', 'timing', 'xevt_id'
            __timing_c = make_immutable_slots_class(Slots.__slots__)
            __timing_is = __timing_c(__timing)

            __tuned_values.update({'timing': __timing_is})

            Slots.__slots__ = 'arguments', 'command', 'success_chance', 'timing'
            __tuned_values_c = make_immutable_slots_class(Slots.__slots__)
            __tuned_values_is = __tuned_values_c(__tuned_values)

            _tuned_values = __tuned_values_is
            basic_extras = TunableFactory.TunableFactoryWrapper(_tuned_values, 'TunableDoCommand', interactions.utils.tunable.DoCommand)

        except Exception as e:
            log.error(f"Failed to process: '{e}'")

        return basic_extras


'''
create_basic_extras() creates this 'basic_extras' object:
_tuned_values = ImmutableSlots({
    'arguments': (
        ImmutableSlots({
            'arg_type': <CommandArgType.ARG_TYPE_STRING = 1>,
            'argument': '{parameter}'
        }),
        ImmutableSlots({
            'arg_type': <CommandArgType.ARG_TYPE_BOOL = 0>,
            'argument': <ParticipantType.Actor = 1>
        }),
        ImmutableSlots({
            'arg_type': <CommandArgType.ARG_TYPE_BOOL = 0>,
            'argument': <ParticipantType.TargetSim = 1>
        })
    ),
    'command': '{command}',
    'success_chance': SuccessChance(base_chance=1.0, multipliers=()),
    'timing': ImmutableSlots({
        'criticality': <CleanupType.OnCancel = 1>,
        'offset_time': {offset_time},
        'supports_failsafe': None,
        'timing': '{timing}',
        'xevt_id': {xevt_id}
    })
})
basic_extras = TunableFactory.TunableFactoryWrapper(_tuned_values, 'TunableDoCommand', interactions.utils.tunable.DoCommand)
'''
