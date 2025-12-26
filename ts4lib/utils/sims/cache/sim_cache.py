#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Set, Dict, Tuple, List, Union

import services
from sims.sim_info import SimInfo
from ts4lib.custom_enums.custom_age import CustomAge
from ts4lib.custom_enums.custom_gender import CustomGender
from ts4lib.custom_enums.custom_occult_type import CustomOccultType
from ts4lib.custom_enums.custom_species import CustomSpecies

from ts4lib.modinfo import ModInfo
from ts4lib.utils.sims.cache.const.sim_cache_definition import SimCacheDefinition

from ts4lib.utils.singleton import Singleton

from sims4communitylib.events.event_handling.common_event_registry import CommonEventRegistry
from sims4communitylib.events.zone_spin.events.zone_teardown import S4CLZoneTeardownEvent
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from sims4communitylib.utils.sims.common_age_utils import CommonAgeUtils
from sims4communitylib.utils.sims.common_gender_utils import CommonGenderUtils
from sims4communitylib.utils.sims.common_occult_utils import CommonOccultUtils
from sims4communitylib.utils.sims.common_sim_name_utils import CommonSimNameUtils
from sims4communitylib.utils.sims.common_species_utils import CommonSpeciesUtils

mod_name = ModInfo.get_identity().name
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), mod_name)
log.enable()
log.info(f"Starting {mod_name}")


class SimCache(object, metaclass=Singleton):

    def __init__(self):
        self.is_ready: bool = False
        self._sims: Dict = {}  # {sim_id: { sim_data }, ...}

        self._sim_ids: Set = set()  # Store all processed _sim_ids, also for pets etc.
        self._sim_names: Dict = {}  # {'sim_search_name': sim_id, ...}

        self._gender_female: Set = set()   # sim_id
        self._gender_male: Set = set()   # sim_id

        self._age_baby: Set = set()  # sim_id
        self._age_infant: Set = set()
        self._age_toddler: Set = set()
        self._age_child: Set = set()
        self._age_teen: Set = set()
        self._age_young_adult: Set = set()
        self._age_adult: Set = set()
        self._age_elder: Set = set()
        self._age_tyae: Set = set()

        self._occult_human: Set = set()  # sim_id
        self._occult_alien: Set = set()
        self._occult_ghost: Set = set()
        self._occult_mermaid: Set = set()
        self._occult_plant_sim: Set = set()
        self._occult_robot: Set = set()
        self._occult_scarecrow: Set = set()
        self._occult_skeleton: Set = set()
        self._occult_vampire: Set = set()
        self._occult_werewolf: Set = set()
        self._occult_witch: Set = set()

        self._species_human: set = set()
        self._species_animal: set = set()
        self._species_cat: set = set()
        self._species_dog: set = set()
        self._species_fox: set = set()
        self._species_horse: set = set()
        self._species_large_dog: set = set()
        self._species_pet: set = set()
        self._species_small_dog: set = set()

    def init(self):
        self._sims: Dict = {}  # {sim_id: { sim_data }, ...}

        self._sim_ids: Set = set()  # Store all processed _sim_ids, also for pets etc.
        self._sim_names: Dict = {}  # {'sim_name': sim_id, ...}

        self._gender_female: Set = set()  # {sim_id: 'sim_name', ...}
        self._gender_male: Set = set()  # {sim_id: 'sim_name', ...}

        self._age_baby: Set = set()  # sim_id
        self._age_infant: Set = set()
        self._age_toddler: Set = set()
        self._age_child: Set = set()
        self._age_teen: Set = set()
        self._age_young_adult: Set = set()
        self._age_adult: Set = set()
        self._age_elder: Set = set()
        self._age_tyae: Set = set()

        self._occult_human: Set = set()
        self._occult_alien: Set = set()
        self._occult_ghost: Set = set()
        self._occult_mermaid: Set = set()
        self._occult_plant_sim: Set = set()
        self._occult_robot: Set = set()
        self._occult_scarecrow: Set = set()
        self._occult_skeleton: Set = set()
        self._occult_vampire: Set = set()
        self._occult_werewolf: Set = set()
        self._occult_witch: Set = set()

        self._species_human: set = set()
        self._species_animal: set = set()
        self._species_cat: set = set()
        self._species_dog: set = set()
        self._species_fox: set = set()
        self._species_horse: set = set()
        self._species_large_dog: set = set()
        self._species_pet: set = set()
        self._species_small_dog: set = set()

    @property
    def sim_ids(self):
        self.update_sim_ids()
        return self._sim_ids.copy()

    @property
    def sim_names(self):
        self.update_sim_ids()
        return self._sim_names.copy()

    @property
    def sims(self):
        return self._sims.copy()

    @property
    def gender_females(self):
        self.update_sim_ids()
        return self._gender_female.copy()

    @property
    def gender_males(self):
        self.update_sim_ids()
        return self._gender_male.copy()

    @property
    def age_baby(self):
        self.update_sim_ids()
        return self._age_baby.copy()

    @property
    def age_infant(self):
        self.update_sim_ids()
        return self._age_infant.copy()

    @property
    def age_toddler(self):
        self.update_sim_ids()
        return self._age_toddler.copy()

    @property
    def age_child(self):
        self.update_sim_ids()
        return self._age_child.copy()

    @property
    def age_teen(self):
        self.update_sim_ids()
        return self._age_teen.copy()

    @property
    def age_young_adult(self):
        self.update_sim_ids()
        return self._age_young_adult.copy()

    @property
    def age_adult(self):
        self.update_sim_ids()
        return self._age_adult.copy()

    @property
    def age_elder(self):
        self.update_sim_ids()
        return self._age_elder.copy()

    @property
    def age_tyae(self):
        self.update_sim_ids()
        return self._age_tyae.copy()

    @property
    def occult_human(self):
        self.update_sim_ids()
        return self._occult_human.copy()

    @property
    def occult_alien(self):
        self.update_sim_ids()
        return self._occult_alien.copy()

    @property
    def occult_vampire(self):
        self.update_sim_ids()
        return self._occult_vampire.copy()

    @property
    def occult_mermaid(self):
        self.update_sim_ids()
        return self._occult_mermaid.copy()

    @property
    def occult_witch(self):
        self.update_sim_ids()
        return self._occult_witch.copy()

    @property
    def occult_werewolf(self):
        self.update_sim_ids()
        return self._occult_werewolf.copy()

    @property
    def occult_ghost(self):
        self.update_sim_ids()
        return self._occult_ghost.copy()

    @property
    def occult_robot(self):
        self.update_sim_ids()
        return self._occult_robot.copy()

    @property
    def occult_scarecrow(self):
        self.update_sim_ids()
        return self._occult_scarecrow.copy()

    @property
    def occult_skeleton(self):
        self.update_sim_ids()
        return self._occult_skeleton.copy()

    @property
    def occult_plant_sim(self):
        self.update_sim_ids()
        return self._occult_plant_sim.copy()

    @property
    def species_human(self):
        self.update_sim_ids()
        return self._species_human.copy()

    @property
    def species_animal(self):
        self.update_sim_ids()
        return self._species_animal.copy()

    @property
    def species_cat(self):
        self.update_sim_ids()
        return self._species_cat.copy()

    @property
    def species_dog(self):
        self.update_sim_ids()
        return self._species_dog.copy()

    @property
    def species_fox(self):
        self.update_sim_ids()
        return self._species_fox.copy()

    @property
    def species_horse(self):
        self.update_sim_ids()
        return self._species_horse.copy()

    @property
    def species_large_dog(self):
        self.update_sim_ids()
        return self._species_large_dog.copy()

    @property
    def species_pet(self):
        self.update_sim_ids()
        return self._species_pet.copy()

    @property
    def species_small_dog(self):
        self.update_sim_ids()
        return self._species_small_dog.copy()

    def sim_name(self, sim_id: int) -> str:
        return self.sims.get(sim_id, {}).get('sim_name', None)

    def search_name(self, sim_id: int) -> str:
        """ sim_name in lower case """
        return self.sims.get(sim_id, {}).get('search_name', None)

    def age(self, sim_id: int) -> str:
        """ sim_name in lower case """
        return self.sims.get(sim_id, {}).get('age', None)

    def gender_types(self, sim_id: int) -> Set[str]:
        """ sim_name in lower case """
        return self.sims.get(sim_id, {}).get('gender_types', None)

    def occult_types(self, sim_id: int) -> Set[str]:
        """ sim_name in lower case """
        return self.sims.get(sim_id, {}).get('occult_types', None)

    def species(self, sim_id: int) -> Set[str]:
        """ sim_name in lower case """
        return self.sims.get(sim_id, {}).get('species', None)

    def update_sim_ids(self, force_refresh: bool = False):
        if force_refresh:
            self.is_ready = False
        if self.is_ready:
            return
        self.init()
        all_sim_info = services.sim_info_manager().get_all()
        for _sim_info in all_sim_info:
            sim_info: SimInfo = _sim_info
            sim_id = 0
            sim_name = search_name = f'unknown firstname{SimCacheDefinition.SIM_NAMES_SEP}unknown lastname'
            age: str = f"{CustomAge.INVALID}"
            gender_types = set()
            occult_types = set()
            species = set()

            try:
                if not sim_info:
                    log.warn(f"Failed to get sim_info for _sim_info: {_sim_info}")
                    continue
                sim_id: int = sim_info.sim_id
                if not sim_id:
                    log.warn(f"Failed to get sim_id for sim_info: {sim_info}")
                    continue
                if sim_id in self._sim_ids:
                    log.warn(f"Skipping duplicate sim id: {sim_id}")
                    continue
                self._sim_ids.add(sim_id)
                self._sims.update({sim_id: {}})

                f_name = CommonSimNameUtils.get_first_name(sim_info)
                l_name = CommonSimNameUtils.get_last_name(sim_info)
                sim_name = f"{f_name}{SimCacheDefinition.SIM_NAMES_SEP}{l_name}"
                search_name = sim_name.lower()
                self._sim_names.update({search_name: sim_id})
            except Exception as e:
                log.warn(f"Failed to get sim_name for sim_id: {sim_id} ({e}")

            try:
                is_female = CommonGenderUtils.is_female(sim_info)
                if is_female:
                    self._gender_female.add(sim_id)
                    gender_types.add('FEMALE')

                is_male = CommonGenderUtils.is_male(sim_info)
                if is_male:
                    self._gender_male.add(sim_id)
                    gender_types.add('MALE')
            except Exception as e:
                log.warn(f"Failed to get genders for sim_id: {sim_id} ({e}")

            try:
                # Process the occults which are not handled by TS4 as occults:
                if CommonOccultUtils.is_alien(sim_info):
                    self._occult_alien.add(sim_id)
                    occult_types.add(CustomOccultType.ALIEN)
                if CommonOccultUtils.is_ghost(sim_info):
                    self._occult_ghost.add(sim_id)
                    occult_types.add(CustomOccultType.GHOST)
                if CommonOccultUtils.is_mermaid(sim_info):
                    self._occult_mermaid.add(sim_id)
                    occult_types.add(CustomOccultType.MERMAID)
                if CommonOccultUtils.is_plant_sim(sim_info):
                    self._occult_plant_sim.add(sim_id)
                    occult_types.add(CustomOccultType.PLANT_SIM)
                if CommonOccultUtils.is_robot(sim_info):
                    self._occult_robot.add(sim_id)
                    occult_types.add(CustomOccultType.ROBOT)
                if CommonOccultUtils.is_scarecrow(sim_info):
                    self._occult_scarecrow.add(sim_id)
                    occult_types.add(CustomOccultType.SCARECROW)
                if CommonOccultUtils.is_skeleton(sim_info):
                    self._occult_skeleton.add(sim_id)
                    occult_types.add(CustomOccultType.SKELETON)
                if CommonOccultUtils.is_vampire(sim_info):
                    self._occult_vampire.add(sim_id)
                    occult_types.add(CustomOccultType.VAMPIRE)
                if CommonOccultUtils.is_witch(sim_info):
                    self._occult_witch.add(sim_id)
                    occult_types.add(CustomOccultType.WITCH)
                if CommonOccultUtils.is_werewolf(sim_info):
                    self._occult_werewolf.add(sim_id)
                    occult_types.add(CustomOccultType.WEREWOLF)

                _is_human = True
                for occult_type in CustomOccultType.__members__.items():
                    if occult_type in occult_types:
                        _is_human = False
                        break
                if _is_human:
                    self._occult_human.add(sim_id)
                    occult_types.add(CustomOccultType.HUMAN)
            except Exception as e:
                log.warn(f"Failed to get occults for sim_id: {sim_id} ({e}")

            try:
                age = f"{CommonAgeUtils.get_age(sim_info)}"
                _age = age.lower()
                _age = _age.replace('age.', '')
                _age = _age.replace('youngadult', 'young_adult')
                age_attribute_name = f"_age_{_age.lower()}"
                _sim_ids = getattr(self, age_attribute_name)
                _sim_ids.add(sim_id)
                setattr(self, age_attribute_name, _sim_ids)
                if _age in ['teen', 'young_adult', 'adult', 'elder']:
                    age_attribute_name = "_age_tyae"
                    self._age_tyae.add(sim_id)
            except Exception as e:
                log.warn(f"Failed to get age for sim_id: {sim_id} ({e}")

            try:
                # Process the species
                if CommonSpeciesUtils.is_human(sim_info):
                    self._species_human.add(sim_id)
                    species.add(CustomSpecies.HUMAN)
                if CommonSpeciesUtils.is_animal(sim_info):
                    self._species_animal.add(sim_id)
                    species.add(CustomSpecies.ANIMAL)
                if CommonSpeciesUtils.is_cat(sim_info):
                    self._species_cat.add(sim_id)
                    species.add(CustomSpecies.CAT)
                if CommonSpeciesUtils.is_dog(sim_info):
                    self._species_dog.add(sim_id)
                    species.add(CustomSpecies.DOG)
                if CommonSpeciesUtils.is_fox(sim_info):
                    self._species_fox.add(sim_id)
                    species.add(CustomSpecies.FOX)
                if CommonSpeciesUtils.is_human(sim_info):
                    self._species_horse.add(sim_id)
                    species.add(CustomSpecies.HORSE)
                if CommonSpeciesUtils.is_large_dog(sim_info):
                    self._species_large_dog.add(sim_id)
                    species.add(CustomSpecies.LARGE_DOG)
                if CommonSpeciesUtils.is_pet(sim_info):
                    self._species_pet.add(sim_id)
                    species.add(CustomSpecies.PET)
                if CommonSpeciesUtils.is_small_dog(sim_info):
                    self._species_small_dog.add(sim_id)
                    species.add(CustomSpecies.SMALL_DOG)
            except Exception as e:
                log.warn(f"Failed to get species for sim_id: {sim_id} ({e}")

            self._sims.update({sim_id: {
                'search_name': search_name,
                'sim_name': sim_name,
                'age': age,
                'gender_types': gender_types,
                'occult_types': occult_types,
                'species': species,
            }})

        self.is_ready = True

    def get_sim_ids_by_occult_types(self, occult_types: List[Union[CustomOccultType, str]]) -> Set:
        """
        Return 0-n _sims matching the specified IDs.
        :param occult_types: List with occult_types, eg ['HUMAN', ]
        :return: (sim_id, ...)
        """
        self.update_sim_ids()
        rv: Set = set()
        for occult_type in occult_types:
            try:
                if isinstance(occult_type, CustomOccultType):
                    occult_type = occult_type.name
                occult_attribute_name = f"_occult_{occult_type.lower()}"
                _sim_ids = getattr(self, occult_attribute_name)
                rv.update(_sim_ids)
            except Exception as e:
                log.warn(f"Oops: {e}")
        return rv

    def get_sim_ids_by_ages(self, ages: List[Union[CustomAge, str]]) -> Set:
        """
        Return 0-n _sims matching the specified IDs.
        :param ages: List with ages, eg ['TEEN', ]
        :return: (sim_id, ...)
        """
        self.update_sim_ids()
        rv: Set = set()
        for age in ages:
            try:
                if isinstance(age, CustomAge):
                    age = age.name
                age_attribute_name = f"_age_{age.lower()}"
                _sim_ids = getattr(self, age_attribute_name)
                rv.update(_sim_ids)
            except Exception as e:
                log.warn(f"Oops: {e}")
        return rv

    def get_sim_ids_by_ids(self, sim_ids: List[int]) -> Set:
        """
        Return 0-n _sims matching the specified IDs.
        :param sim_ids: List with IDs, eg [123, ]
        :return: (sim_id, ...)
        """
        rv: Set = set()
        _known_sim_ids = self.sim_ids  # calls self.update_sim_ids()
        for sim_id in sim_ids:
            if sim_id in _known_sim_ids:
                rv.add(sim_id)
        return rv

    def get_sim_ids_by_genders(self, genders: List[Union[CustomGender, str]]) -> Set:
        """
        Return 0-n _sims matching the specified gender.
        :param genders: ...
        :return: (sim_id, ...)
        """
        self.update_sim_ids()
        rv: Set = set()
        for gender in genders:
            try:
                if isinstance(gender, CustomGender):
                    gender = gender.name
                gender_attribute_name = f"_gender_{gender.lower()}"
                _sim_ids = getattr(self, gender_attribute_name)
                rv.update(_sim_ids)
            except Exception as e:
                log.warn(f"Oops: {e}")
        return rv

    def get_sim_ids_by_sim_name(self, sim_name: str = SimCacheDefinition.SIM_NAMES_SEP) -> Tuple[Set[int], Set[int], Set[int], Set[int], Set[int]]:
        """
        Return 0-n _sims matching the specified sim name.
        Equals, startswith, endswith and contains tests are performed.
        'bella#goth' will likely find one sim named 'Bella#Goth'.
        'be#g' may find a sim named 'Be#G' or 'Bella#Goth', 'Ben#Gur', ... as the fist char(s) match.
        'a#h' may fina a sim named 'A#H' or 'Ann#Hur', ... or 'Bella#Goth', ... as the last char(s) matches.
        'll#ot' may find 'Bella#Goth' as the chars are contained in the name.
        :param sim_name: Full or partial sim name with '#' to separate first and last name. Default is '#' so all _sims are returned.
        :return: Tuple with x_match, equals_match, starts_match, ends_match, contains_match. x_match is the best match of the 4 following values.
        x_match should be used unless one is interested in other name matches.
        """
        self.update_sim_ids()
        if not sim_name:
            sim_name = f"{sim_name}#"
        short_first_name, short_last_name = sim_name.lower().split(SimCacheDefinition.SIM_NAMES_SEP, 1)
        equals_match: Set = set()
        starts_match: Set = set()
        ends_match: Set = set()
        contains_match: Set = set()
        for search_name, sim_id in self.sim_names.items():
            _first_name, _last_name = search_name.split(SimCacheDefinition.SIM_NAMES_SEP, 1)
            if (_first_name == short_first_name) and (_last_name == short_last_name):
                equals_match.add(sim_id)
            elif _first_name.startswith(short_first_name) and _last_name.startswith(short_last_name):
                starts_match.add(sim_id)
            elif _first_name.endswith(short_first_name) and _last_name.endswith(short_last_name):
                ends_match.add(sim_id)
            elif short_first_name in _first_name and short_last_name in _last_name:
                contains_match.add(sim_id)

        if equals_match:
            return equals_match, equals_match, starts_match, ends_match, contains_match
        elif starts_match:
            return starts_match, equals_match, starts_match, ends_match, contains_match
        elif ends_match:
            return ends_match, equals_match, starts_match, ends_match, contains_match
        else:
            return contains_match, equals_match, starts_match, ends_match, contains_match

    @staticmethod
    @CommonEventRegistry.handle_events(ModInfo.get_identity())
    def handle_event(event_data: S4CLZoneTeardownEvent):
        log.debug(f"Invalidating cache")
        sc = SimCache()
        sc.is_ready = False  # Set is_ready to force a refresh when entering a lot.
