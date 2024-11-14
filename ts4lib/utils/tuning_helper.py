#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import time
from typing import Dict, Set, Union, List, Tuple, Any

import services
import sims4
import sims4.commands
from interactions import ParticipantType
from objects.definition_manager import DefinitionManager
from server_commands.tuning_commands import get_managers
from sims.sim_info_tests import TraitTest, BuffTest
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


    def modify_test_globals(self, tuning_dict: Dict, no_gender_check: bool = False,  gender: Union[str, None] = None, who: ParticipantType = ParticipantType.Actor,
                            add_whitelist_traits: Union[Set, None] = None, remove_whitelist_traits: Union[Set, bool] = False,
                            add_blacklist_traits: Union[Set, None] = None, remove_blacklist_traits: Union[Set, bool] = False,
                            add_whitelist_buffs: Union[Set, None] = None, remove_whitelist_buffs: Union[Set, bool] = False,
                            add_blacklist_buffs: Union[Set, None] = None, remove_blacklist_buffs: Union[Set, bool] = False):
        """
        @param no_gender_check: True: Remove gender check, don't specify gender in this case
        @param gender: 'MALE', 'FEMALE', None
        @param who: ParticipantType.Actor / .TargetSim
        @param remove_blacklist_buffs: Set to True to remove all blacklist buffs
        @param remove_whitelist_traits: Set to True to remove all whitelist traits

        not yet implemented: SimInfoTest(ages=frozenset({<Age.TEEN = 8>, <Age.YOUNGADULT = 16>, <Age.ADULT = 32>, <Age.ELDER = 64>}), can_age_up=None, gender=Gender.FEMALE, has_been_played=None, is_active_sim=None, match_type=MatchType.MATCH_ALL, npc=None, species=_SpeciesTestSpecies(species=frozenset({<Species.HUMAN = 1>})), tooltip=None, who=ParticipantType.Actor)
        not yet implemented: BuffTest:whitelist
        not yet implemented: TraitTest:blacklist_traits
        """
        for tuning_id, data in tuning_dict.items():
            tuning, _, tuning_name = data
            try:
                test_globals = getattr(tuning, 'test_globals', None)
                if self.verbose:
                    log.debug(f"modify_test_globals({tuning_name} ({tuning_id}) -> test_globals: {(type(test_globals))} = {test_globals}")
                for test_class in test_globals:
                    if self.verbose:
                        log.debug(f"test_class: '{type(test_class)}' = '{test_class}'")

                    if isinstance(test_class, TraitTest):
                        if add_whitelist_traits or remove_whitelist_traits:
                            whitelist_traits = getattr(test_class, 'whitelist_traits', set())
                            if self.verbose:
                                log.debug(f"whitelist_traits {whitelist_traits}")
                            new_whitelist_traits = add_whitelist_traits if add_whitelist_traits else set()
                            if remove_whitelist_traits is False:
                                new_whitelist_traits.update(set(whitelist_traits))  # default: keep all traits
                            elif isinstance(new_whitelist_traits, set):  # remove the tunings in this Set[tunings]
                                for whitelist_trait in whitelist_traits:
                                    # Keep whitelist buffs unless they are in remove_whitelist_traits
                                    if whitelist_trait not in remove_whitelist_traits:
                                        new_whitelist_traits.add(whitelist_trait)
                            # else: pass  # # drop the original whitelist_traits
                            if self.verbose:
                                log.debug(f"new_whitelist_traits {new_whitelist_traits}")
                            setattr(test_class, 'whitelist_traits', tuple(new_whitelist_traits))
                        if add_blacklist_traits or remove_blacklist_traits:
                            blacklist_traits = getattr(test_class, 'blacklist_traits', set())
                            if self.verbose:
                                log.debug(f"blacklist_traits {blacklist_traits}")
                            new_blacklist_traits = add_blacklist_traits if add_blacklist_traits else set()
                            if remove_blacklist_traits is False:
                                new_blacklist_traits.update(set(blacklist_traits))  # default: keep all traits
                            elif isinstance(new_blacklist_traits, set):  # remove the tunings in this Set[tunings]
                                for blacklist_trait in blacklist_traits:
                                    # Keep blacklist buffs unless they are in remove_blacklist_traits
                                    if blacklist_trait not in remove_blacklist_traits:
                                        new_blacklist_traits.add(blacklist_trait)
                            # else: pass  # # drop the original blacklist_traits
                            if self.verbose:
                                log.debug(f"new_blacklist_traits {new_blacklist_traits}")
                            setattr(test_class, 'blacklist_traits', tuple(new_blacklist_traits))

                    if isinstance(test_class, BuffTest):
                        if add_whitelist_buffs or remove_whitelist_buffs:
                            whitelist_buffs = getattr(test_class, 'whitelist', set())
                            if self.verbose:
                                log.debug(f"whitelist_buffs {whitelist_buffs}")
                            new_whitelist_buffs = add_whitelist_buffs if add_whitelist_buffs else set()
                            if remove_whitelist_buffs is False:
                                new_whitelist_buffs.update(set(whitelist_buffs))  # default: keep all buffs
                            elif isinstance(remove_whitelist_buffs, set):  # remove the tunings in this Set[tunings]
                                for whitelist_buff in whitelist_buffs:
                                    # Keep whitelist buffs unless they are in remove_whitelist_buffs
                                    if whitelist_buff not in remove_whitelist_buffs:
                                        new_whitelist_buffs.add(whitelist_buff)
                            # else: pass  # drop the original whitelist_buffs
                            if self.verbose:
                                log.debug(f"new_whitelist_buffs {new_whitelist_buffs}")
                            setattr(test_class, 'whitelist', tuple(new_whitelist_buffs))
                        if add_blacklist_buffs or remove_blacklist_buffs:
                            blacklist_buffs = getattr(test_class, 'blacklist', set())
                            if self.verbose:
                                log.debug(f"blacklist_buffs {blacklist_buffs}")
                            new_blacklist_buffs = add_blacklist_buffs if add_blacklist_buffs else set()
                            if remove_blacklist_buffs is False:
                                new_blacklist_buffs.update(set(blacklist_buffs))  # default: keep all buffs
                            elif isinstance(remove_blacklist_buffs, set):  # remove the tunings in this Set[tunings]
                                for blacklist_buff in blacklist_buffs:
                                    # Keep blacklist buffs unless they are in remove_blacklist_buffs
                                    if blacklist_buff not in remove_blacklist_buffs:
                                        new_blacklist_buffs.add(blacklist_buff)
                            # else: pass  # drop the original blacklist_buffs
                            if self.verbose:
                                log.debug(f"new_blacklist_buffs {new_blacklist_buffs}")
                            setattr(test_class, 'blacklist', tuple(new_blacklist_buffs))

                    if no_gender_check or gender:
                        _who = getattr(test_class, 'who', None)
                        _gender = getattr(test_class, 'gender', None)
                        if self.verbose:
                            log.debug(f"who {_who}: {type(_who)}; gender {_gender}: {type(_gender)}")
                        setattr(test_class, 'gender', gender)
                        if not _who:
                            setattr(test_class, 'who', who)

            except Exception as e:
                log.warn(f"modify_test_globals({tuning_name} ({tuning_id}) failed altering tuning: '{e}'")
