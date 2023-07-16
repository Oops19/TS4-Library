#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2022 https://github.com/Oops19
#


from typing import Union, Tuple

import sims4
import sims4.commands
import services
import interactions
from sims4.resources import get_resource_key
from interactions.utils.success_chance import SuccessChance
from interactions.utils.tunable import DoCommand
from interactions import ParticipantType

from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog
from ts4lib.modinfo import ModInfo
from ts4lib.utils.tuning_helper import TuningHelper

log: CommonLog = CommonLogRegistry.get().register_log(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name)
log.enable()


class BasicExtras:
    @staticmethod
    def add_do_command(manager: str, tunings: list, command: str, parameter: str, timing: str = 'at_end',
                       offset_time: Union[None, float] = None, xevt_id: Union[None, int] = None):
        log.debug(f"add_do_command({manager}, {tunings}, {command}, {parameter}, {timing}, {offset_time}, {xevt_id})")
        tuning_dict = TuningHelper().get_tuning_dict(manager, tunings)
        instance_manager = services.get_instance_manager(sims4.resources.Types[manager])
        for tuning_id, tuning_name in tuning_dict.items():
            log.debug(f"Processing '{tuning_name}({tuning_id})'")
            tuning = instance_manager.get(tuning_id)
            if tuning:
                basic_extra = BasicExtras.create_basic_extras(command, f"{tuning_name}+{parameter}", timing, offset_time, xevt_id)
                basic_extras: Tuple = (basic_extra,)

                if getattr(tuning, 'basic_extras', None):
                    # Add the new command to 'basic_extras'
                    for basic_extra in getattr(tuning, 'basic_extras'):
                        if (getattr(basic_extra, 'command', None) == command) and (getattr(basic_extra, 'argument', None) == parameter):
                            log.debug(f"Tuning already contains command '{command}({parameter})'")
                            continue
                        basic_extras += (basic_extra,)

                setattr(tuning, 'basic_extras', basic_extras)
                log.debug(f"New basic_extras: {getattr(tuning, 'basic_extras', None)}")
            else:
                log.warn(f"Didn't find '{tuning_name}({tuning_id})'")

    @staticmethod
    def create_basic_extras(command: str, parameter: str = '', timing: str = 'at_end', offset_time: Union[None, float] = None, xevt_id: Union[None, int] = None):
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
            __tuned_values.update({'success_chance': SuccessChance.ONE})

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

            '''
            __tuned_values.update({'arguments': (__arguments_t1_is, __arguments_t2_is, )})
            '''

            __arguments_t3 = dict()
            __arguments_t3.update({'arg_type': CommandArgType.ARG_TYPE_BOOL})
            __arguments_t3.update({'argument': ParticipantType.TargetSim})
            Slots.__slots__ = 'arg_type', 'argument'
            __arguments_t3_c = make_immutable_slots_class(Slots.__slots__)
            __arguments_t3_is = __arguments_t3_c(__arguments_t3)

            __tuned_values.update({'arguments': (__arguments_t1_is, __arguments_t2_is, __arguments_t3_is,)})

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
