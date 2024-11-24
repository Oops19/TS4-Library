#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import time
from typing import Dict, Set, Union, List, Tuple, Any

import services
import sims4
import sims4.commands
from event_testing.tests import CompoundTestList, TestList
from interactions import ParticipantType
from objects.definition_manager import DefinitionManager
from server_commands.tuning_commands import get_managers

from statistics.skill_tests import SkillRangeTest
from sims.sim_info_tests import TraitTest, BuffTest, SimInfoTest
from event_testing.test_variants import CareerGigTest
from event_testing.statistic_tests import CommodityAdvertisedTest

from sims4.resources import get_resource_key
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class TuningHelper(object, metaclass=Singleton):

    def __init__(self):
        self.manager = None
        self.dt_sum = 0
        self.verbose = False

    def get_tunings(self, manager: Union[None, str], tuning_names: Union[List[str], Set[int]]) -> Set[Any]:
        """
        :param manager: see @get_tuning_dict
        :param tuning_names: see @get_tuning_dict
        :return: A set with all matching tunings (tuning instances).
        """
        tuning_dict = self.get_tuning_dict(manager, tuning_names)
        tunings = set()
        for _tuning_id, data in tuning_dict.items():
            tuning, _manager_str, _tuning_name = data
            tunings.add(tuning)
        return tunings

    def get_tuning_ids(self, manager: Union[None, str], tuning_names: Union[List[str], Set[int]]) -> Set[int]:
        """
        :param manager: see @get_tuning_dict
        :param tuning_names: see @get_tuning_dict
        :return: A set with all matching tuning IDs.
        """
        tuning_dict = self.get_tuning_dict(manager, tuning_names)
        return set(tuning_dict.keys())

    def get_tuning_dict(self, manager: Union[None, str], tuning_names: Union[List[str], Set[int]]) -> Dict[int, Tuple[Any, str, str]]:
        """
        Interactive usage is fine, monitor times when using it in production and if it is called multiple times.
        This method is slow as it creates a dict and does not only return the tunings.
        :param manager: Identifier to select an instance_manager. Eg BUFF, TRAIT, ... 'None' will iterate over all manager and this will take some time!
        :param tuning_names: A list with tuning IDs as strings for this instance_manager.
        Supported formats: * '123' or '0xabc' to specify the tuning ID directly.
        * ' 123' or ' 0xabc' to specify a tuning name which looks like a number
        * 'tuning_name' to specify a full name, eg: 'buff_sleep' or something like this
        * 'tuning_*' to specify all tuning_names which start with 'tuning_'
        * '*_name' to specify all tuning_names which end with '_name'
        * '*g_n*' to specify all tuning_names which contain 'g_n'
        * '*' to get all tuning_names for the specified instance_manager.
        :return: A dict with the tuning_id and the (tuning, instance_manager_str and tuning_name). If wildcards have been used many tuning_ids and tuning_names may be returned.
        :return {tuning_id: (tuning, f"{instance_manager.TYPE.name}", f"{get_tuning_name(tuning)})
        """
        t = time.time()
        self.manager = manager
        log.debug(f"get_tuning_dict({manager}: {type(manager)}, {tuning_names}: {type(tuning_names)})")
        if manager is not None:
            rt_manager = manager.upper()
            instance_manager = services.get_instance_manager(sims4.resources.Types[rt_manager])
            tuning_dict = self._get_tuning_dict(instance_manager, manager, tuning_names)
        else:
            tuning_dict: dict = {}
            managers = get_managers()
            for manager in managers:
                if manager == 'objects':
                    continue
                instance_manager = managers.get(manager, None)
                tuning_dict = {**tuning_dict, **self._get_tuning_dict(instance_manager, manager, tuning_names)}
        dt = time.time() - t
        self.dt_sum += dt
        log.debug(f"get_tuning_dict() duration: {dt:.3f}s (sum: {self.dt_sum:.3f} s) -> '{tuning_dict}'")
        return tuning_dict

    def _get_tuning_dict(self, instance_manager, manager, tuning_names: Union[List[str], Set[int]]) -> Dict[int, Tuple[Any, str, str]]:
        """
        :param instance_manager: An instance_manager.
        :param manager: see @get_tuning_dict
        :param tuning_names: see @get_tuning_dict
        :return: see @get_tuning_dict
        """
        tuning_dict = dict()
        for tuning_name in tuning_names:
            if f"{tuning_name}".isdecimal():
                try:
                    _tuning_id = int(tuning_name)
                    key = get_resource_key(_tuning_id, instance_manager.TYPE)
                    tuning_dict.update(self._dict(instance_manager, manager, key, tuning_name))
                except:
                    log.error(f"Could not convert '{tuning_name}'", throw=True)
                continue

            if tuning_name.startswith('0x'):
                try:
                    _tuning_id = int(tuning_name, 16)
                    key = get_resource_key(_tuning_id, instance_manager.TYPE)
                    tuning_dict.update(self._dict(instance_manager, manager, key, tuning_name))
                except:
                    log.error(f"Could not convert '{tuning_name}'", throw=False)
                continue

            tuning_name = tuning_name.lower().strip()
            if tuning_name == '*':
                for (key, tuning_file) in instance_manager.types.items():
                    tuning_dict.update(self._dict(instance_manager, manager, key, tuning_name))

            elif tuning_name.startswith('*'):
                if tuning_name.endswith('*'):
                    tuning_name = tuning_name[1:-1]
                    for (key, tuning_file) in instance_manager.types.items():
                        if f"{tuning_file.__name__.lower()}" in tuning_name:
                            tuning_dict.update(self._dict(instance_manager, manager, key, tuning_name))

                else:
                    tuning_name = tuning_name[1:]
                    for (key, tuning_file) in instance_manager.types.items():
                        if f"{tuning_file.__name__.lower()}".endswith(tuning_name):
                            tuning_dict.update(self._dict(instance_manager, manager, key, tuning_name))

            elif tuning_name.endswith('*'):
                tuning_name = tuning_name[:-1]
                for (key, tuning_file) in instance_manager.types.items():
                    if f"{tuning_file.__name__.lower()}".startswith(tuning_name):
                        tuning_dict.update(self._dict(instance_manager, manager, key, tuning_name))

            else:
                for (key, tuning_file) in instance_manager.types.items():
                    if f"{tuning_file.__name__.lower()}" == tuning_name:
                        d = self._dict(instance_manager, manager, key, tuning_name)
                        if d:
                            tuning_dict.update(d)
        if self.manager or tuning_dict:
            log.debug(f"Tunings: '{tuning_dict}' for '{tuning_names}'")
        return tuning_dict

    def _dict(self, instance_manager, manager, key, tuning_name):
        def get_tuning_name(tuning) -> str:
            # 'BUFF's no longer support .__name__
            try:
                return f"{tuning.__name__}"
            except:
                return f"{str(tuning)}"

        try:
            if manager == 'OBJECT':
                try:
                    int_key = int(f"0x{key}".split('!')[1].split('.')[0].replace("'", ""), 16)
                    definition_manager = services.definition_manager()
                    tuning = super(DefinitionManager, definition_manager).get(int_key)
                    try:
                        log.debug(f"{int_key} - {tuning} - {instance_manager.TYPE.name} - {get_tuning_name(tuning)}")
                        return {int_key: (tuning, f"{instance_manager.TYPE.name}", f"{get_tuning_name(tuning)}")}
                    except:
                        log.debug(f"{int_key} - {tuning} - {instance_manager.TYPE.name} - {key}")
                        return {int_key: (tuning, f"{instance_manager.TYPE.name}", f"{key}")}
                except:
                    log.error(f"Error: '_dict({instance_manager}, {manager}, {key}, {tuning_name})", throw=True)
                    return {}

            tuning = instance_manager.get(key)
            # if TuningHelper.manager is not None and tuning is None:
            if tuning is None:
                if self.manager:
                    log.debug(f"Skipping: {key.instance}: ({tuning}, {manager}, {tuning_name}")
                return {}
            return {key.instance: (tuning, f"{instance_manager.TYPE.name}", f"{get_tuning_name(tuning)}")}
        except:
            log.error(f"Error: '_dict({instance_manager}, {manager}, {key}, {tuning_name})", throw=True)
            return {}

    # noinspection PyMethodMayBeStatic
    def disable_gender_check(self, _manager: str, tuning_ids: set):
        """
        Deprecated, call `modify_test_globals(tuning_dict, no_gender_check=True)` instead
        @param _manager:
        @param tuning_ids:
        @return:
        """
        instance_manager = services.get_instance_manager(sims4.resources.Types[_manager])
        for tuning_id in tuning_ids:
            try:
                tuning = instance_manager.get(tuning_id)
                test_globals = getattr(tuning, 'test_globals', None)
                for test_global in test_globals:
                    who = getattr(test_global, 'who', None)
                    if who == ParticipantType.Actor:
                        setattr(test_global, 'gender', None)
            except Exception as e:
                log.debug(f"Fail tuning_id '{tuning_id}': '{e}'")

    def remove_privacy(self, tuning_dict: Dict):
        """
        Removes the 'privacy' property from tunings.
        """
        if tuning_dict:
            for _tuning_id, tuning_data in tuning_dict.items():
                tuning, _manager, tuning_name = tuning_data
                setattr(tuning, 'privacy', None)

    def remove_test_globals_test(self, tuning_dict: Dict, remove_test: str):
        """
        Calling this function can cause issues in case further tests require the result of the test itself.
        It removes a complete test class from test_globals for the specified tunings.
        @param tuning_dict:
        @param remove_test: Supported tests: SkillRangeTest, TraitTest, BuffTest, SimInfoTest, CareerGigTest, CommodityAdvertisedTest
        @return:
        """
        _map = {
            'SkillRangeTest': SkillRangeTest,
            'TraitTest': TraitTest,
            'BuffTest': BuffTest,
            'SimInfoTest': SimInfoTest,
            'CareerGigTest': CareerGigTest,
            'CommodityAdvertisedTest': CommodityAdvertisedTest,
        }
        if self.verbose:
            log.debug(f"remove_test_globals_test({tuning_dict}, remove_tests={remove_test})")
        if remove_test in _map.keys():
            rm_test = _map.get(remove_test)
        else:
            log.warn(f"remove_test_globals_test() - Can't remove test '{remove_test}'")
            return
        for tuning_id, data in tuning_dict.items():
            tuning, _, tuning_name = data
            try:
                test_globals = getattr(tuning, 'test_globals', None)
                if self.verbose:
                    log.debug(f"test_globals: {(type(test_globals))} = {test_globals}")
                if isinstance(test_globals, TestList):

                    delete_tests: List = []
                    for test_class in test_globals:
                        if self.verbose:
                            log.debug(f"test_globals.test_class: '{type(test_class)}' = '{test_class}'")
                        if isinstance(test_class, rm_test):
                            delete_tests.append(test_class)
                    for delete_test in delete_tests:
                        test_globals.remove(delete_test)
                if self.verbose:
                    log.debug(f"test_globals: {(type(test_globals))} = {test_globals} <<< NOW")
            except Exception as e:
                log.warn(f"remove_test_globals_test({tuning_name} ({tuning_id}) failed altering tuning: '{e}'")

    def remove_skill_test(self, tuning_dict: Dict):
        """ deprecated, call remove_test_globals_test(tuning_dict, 'SkillRangeTest') """
        """ TODO add to modify_test_globals"""
        if self.verbose:
            log.debug(f"remove_skill_test({tuning_dict})")
        for tuning_id, data in tuning_dict.items():
            tuning, _, tuning_name = data
            try:
                test_globals = getattr(tuning, 'test_globals', None)
                if self.verbose:
                    log.debug(f"test_globals: {(type(test_globals))} = {test_globals}")
                if isinstance(test_globals, TestList):
                    delete_tests: List = []
                    for test_class in test_globals:
                        if self.verbose:
                            log.debug(f"test_globals.test_class: '{type(test_class)}' = '{test_class}'")
                        if isinstance(test_class, SkillRangeTest):
                            delete_tests.append(test_class)
                    for delete_test in delete_tests:
                        test_globals.remove(delete_test)

            except Exception as e:
                log.warn(f"remove_skill_test({tuning_name} ({tuning_id}) failed altering tuning: '{e}'")

    def modify_test(self, tuning_dict: Dict,
                            add_whitelist_traits: Union[Set, None] = None, remove_whitelist_traits: Union[Set, bool] = False,
                            add_blacklist_traits: Union[Set, None] = None, remove_blacklist_traits: Union[Set, bool] = False,
                            add_whitelist_buffs: Union[Set, None] = None, remove_whitelist_buffs: Union[Set, bool] = False,
                            add_blacklist_buffs: Union[Set, None] = None, remove_blacklist_buffs: Union[Set, bool] = False):
        """
        whatever
        @param tuning_dict: Dict with Tuning values

        @param add_whitelist_traits: Specify a 'Set' to add traits
        @param remove_whitelist_traits: Specify a 'Set' to remove individual traits. Set to True to remove all traits
        @param add_blacklist_traits: see above
        @param remove_blacklist_traits: see above
        @param add_whitelist_buffs: see above
        @param remove_whitelist_buffs: see above
        @param add_blacklist_buffs: see above
        @param remove_blacklist_buffs: see above
        """
        if self.verbose:
            log.debug(f"modify_test({tuning_dict}, "
                      f"add_whitelist_traits={add_whitelist_traits}, remove_whitelist_traits={remove_whitelist_traits}, "
                      f"add_blacklist_traits={add_blacklist_traits}, remove_blacklist_traits={remove_blacklist_traits}, "
                      f"add_whitelist_buffs={add_whitelist_buffs}, remove_whitelist_buffs={remove_whitelist_buffs}, "
                      f"add_blacklist_buffs={add_blacklist_buffs}, remove_blacklist_buffs={remove_blacklist_buffs})")

        for tuning_id, data in tuning_dict.items():
            tuning, _, tuning_name = data
            try:
                tests = getattr(tuning, 'test', None)
                if self.verbose:
                    log.debug(f"tests: '{type(tests)}' = '{tests}' (? CompoundTestList)")
                if not tests:
                    continue
                if isinstance(tests, CompoundTestList):
                    for test in tests:
                        if self.verbose:
                            log.debug(f"tests.test: '{type(test)}' = '{test}' (? Tuple)")
                        for _test in test:
                            if self.verbose:
                                log.debug(f"tests.test._test: '{type(_test)}' = '{_test}' (? BuffTest or TraitTest)")
                            if not _test:
                                continue

                            if isinstance(_test, TraitTest) and (add_whitelist_traits or remove_whitelist_traits):
                                values = getattr(_test, 'whitelist_traits', set())
                                new_values = self._modify_values(values, add_whitelist_traits, remove_whitelist_traits)
                                if self.verbose:
                                    log.debug(f"whitelist_traits: {values}")
                                    log.debug(f"              >>> {new_values}")
                                setattr(_test, 'whitelist_traits', tuple(new_values))

                            if isinstance(_test, TraitTest) and (add_blacklist_traits or remove_blacklist_traits):
                                values = getattr(_test, 'blacklist_traits', set())
                                new_values = self._modify_values(values, add_blacklist_traits, remove_blacklist_traits)
                                if self.verbose:
                                    log.debug(f"blacklist_traits: {values}")
                                    log.debug(f"              >>> {new_values}")
                                setattr(_test, 'blacklist_traits', tuple(new_values))

                            if isinstance(tests, BuffTest) and (add_whitelist_buffs or remove_whitelist_buffs):
                                values = getattr(_test, 'whitelist', set())
                                new_values = self._modify_values(values, add_whitelist_buffs, remove_whitelist_buffs)
                                if self.verbose:
                                    log.debug(f"whitelist_buffs: {values}")
                                    log.debug(f"             >>> {new_values}")
                                setattr(_test, 'whitelist', tuple(new_values))

                            if isinstance(tests, BuffTest) and (add_blacklist_buffs or remove_blacklist_buffs):
                                values = getattr(_test, 'blacklist', set())
                                new_values = self._modify_values(values, add_blacklist_buffs, remove_blacklist_buffs)
                                if self.verbose:
                                    log.debug(f"blacklist_buffs: {values}")
                                    log.debug(f"             >>> {new_values}")
                                setattr(_test, 'blacklist', tuple(new_values))
            except Exception as e:
                log.warn(f"modify_test({tuning_name} ({tuning_id}) failed altering tuning: '{e}'")

    def _modify_values(self, values: Set, add_values: Union[Set, None] = None, remove_values: Union[Set, bool] = False) -> Set:
        """
        @param values: The values to be modified
        @param add_values: Add items to 'Set' to add them to 'values'
        @param remove_values: Set to True to remove all values. Add items to 'Set' to remove them from 'values'
        @return:
        """
        new_values = set(values)
        if isinstance(remove_values, set):
            for rm_value in remove_values:
                try:
                    new_values.remove(rm_value)  # Try to remove traits
                except:
                    pass
        elif remove_values is True:
            new_values = set()
        if add_values:
            for add_value in add_values:
                new_values.add(add_value)
        return new_values

    def modify_test_globals(self, tuning_dict: Dict, no_gender_check: bool = False,
                            gender: Union[str, None] = None, actor: Union[ParticipantType, None] = None ,
                            add_whitelist_traits: Union[Set, None] = None, remove_whitelist_traits: Union[Set, bool] = False,
                            add_blacklist_traits: Union[Set, None] = None, remove_blacklist_traits: Union[Set, bool] = False,
                            add_whitelist_buffs: Union[Set, None] = None, remove_whitelist_buffs: Union[Set, bool] = False,
                            add_blacklist_buffs: Union[Set, None] = None, remove_blacklist_buffs: Union[Set, bool] = False):
        """
        @param tuning_dict: Dict with Tuning values

        @param no_gender_check: True: Remove gender check, don't specify gender or actor in this case
        @param gender: None, 'MALE', 'FEMALE' - Change the gender check to 'gender'
        @param actor: None, ParticipantType.Actor, ParticipantType.TargetSim - Change the gender check for 'actor'

        @param add_whitelist_traits: Specify a 'Set' to add traits
        @param remove_whitelist_traits: Specify a 'Set' to remove individual traits. Set to True to remove all traits
        @param add_blacklist_traits: see above
        @param remove_blacklist_traits: see above
        @param add_whitelist_buffs: see above
        @param remove_whitelist_buffs: see above
        @param add_blacklist_buffs: see above
        @param remove_blacklist_buffs: see above

        # Could be added: SimInfoTest(ages=frozenset({<Age.TEEN = 8>, <Age.YOUNGADULT = 16>, <Age.ADULT = 32>, <Age.ELDER = 64>}), can_age_up=None, gender=Gender.FEMALE, has_been_played=None, is_active_sim=None, match_type=MatchType.MATCH_ALL, npc=None, species=_SpeciesTestSpecies(species=frozenset({<Species.HUMAN = 1>})), tooltip=None, who=ParticipantType.Actor)
        """

        if self.verbose:
            log.debug(f"modify_test_globals({tuning_dict}, "
                      f"no_gender_check={no_gender_check}, gender={gender}, actor={actor}, "
                      f"add_whitelist_traits={add_whitelist_traits}, remove_whitelist_traits={remove_whitelist_traits}, "
                      f"add_blacklist_traits={add_blacklist_traits}, remove_blacklist_traits={remove_blacklist_traits}, "
                      f"add_whitelist_buffs={add_whitelist_buffs}, remove_whitelist_buffs={remove_whitelist_buffs}, "
                      f"add_blacklist_buffs={add_blacklist_buffs}, remove_blacklist_buffs={remove_blacklist_buffs})")

        for tuning_id, data in tuning_dict.items():
            tuning, _, tuning_name = data
            try:
                test_globals = getattr(tuning, 'test_globals', None)
                if self.verbose:
                    log.debug(f"test_globals: {(type(test_globals))} = {test_globals}")
                for test_class in test_globals:
                    if self.verbose:
                        log.debug(f"test_class: '{type(test_class)}' = '{test_class}'")

                    if isinstance(test_class, TraitTest) and (add_whitelist_traits or remove_whitelist_traits):
                        values = getattr(test_class, 'whitelist_traits', set())
                        new_values = self._modify_values(values, add_whitelist_traits, remove_whitelist_traits)
                        if self.verbose:
                            log.debug(f"whitelist_traits: {values}")
                            log.debug(f"              >>> {new_values}")
                        setattr(test_class, 'whitelist_traits', tuple(new_values))

                    if isinstance(test_class, TraitTest) and (add_blacklist_traits or remove_blacklist_traits):
                        values = getattr(test_class, 'blacklist_traits', set())
                        new_values = self._modify_values(values, add_blacklist_traits, remove_blacklist_traits)
                        if self.verbose:
                            log.debug(f"blacklist_traits: {values}")
                            log.debug(f"              >>> {new_values}")
                        setattr(test_class, 'blacklist_traits', tuple(new_values))

                    if isinstance(test_class, BuffTest) and (add_whitelist_buffs or remove_whitelist_buffs):
                        values = getattr(test_class, 'whitelist', set())
                        new_values = self._modify_values(values, add_whitelist_buffs, remove_whitelist_buffs)
                        if self.verbose:
                            log.debug(f"whitelist_buffs: {values}")
                            log.debug(f"             >>> {new_values}")
                        setattr(test_class, 'whitelist', tuple(new_values))

                    if isinstance(test_class, BuffTest) and (add_blacklist_buffs or remove_blacklist_buffs):
                        values = getattr(test_class, 'blacklist', set())
                        new_values = self._modify_values(values, add_blacklist_buffs, remove_blacklist_buffs)
                        if self.verbose:
                            log.debug(f"blacklist_buffs: {values}")
                            log.debug(f"             >>> {new_values}")
                        setattr(test_class, 'blacklist', tuple(new_values))

                    if no_gender_check or gender:
                        _who = getattr(test_class, 'who', None)
                        _gender = getattr(test_class, 'gender', None)
                        if self.verbose:
                            log.debug(f"who {_who}: {type(_who)}; gender {_gender}: {type(_gender)}")
                        setattr(test_class, 'gender', gender)
                        if not _who:
                            setattr(test_class, 'who', actor)

            except Exception as e:
                log.warn(f"modify_test_globals({tuning_name} ({tuning_id}) failed altering tuning: '{e}'")
