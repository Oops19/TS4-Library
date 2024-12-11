#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Dict, Tuple, Union

from sims.outfits.outfit_enums import OutfitCategory
from sims.sim_info import SimInfo
from sims4communitylib.services.sim.cas.common_sim_outfit_io import CommonSimOutfitIO
from sims4communitylib.utils.cas.common_outfit_utils import CommonOutfitUtils
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.custom_enums.custom_outfit_category import CustomOutfitCategory

from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class OutfitUtilities(object, metaclass=Singleton):
    @staticmethod
    def apply_outfit(sim_info: SimInfo, parts: Dict, outfit_cat_and_idx: Tuple[Union[CustomOutfitCategory, OutfitCategory, int], int] = (OutfitCategory.SPECIAL, 0)):
        """
        :param sim_info: The sim_info to apply the outfit to
        :param parts: The parts to apply
        :param outfit_cat_and_idx: optional, default: (OutfitCategory.SPECIAL, 0): Tuple
        :return:
        """
        outfit_category, outfit_index = outfit_cat_and_idx

        log.debug(f"apply_outfit({sim_info}, {outfit_category}, {outfit_index}, {parts})")
        outfit_category: OutfitCategory = OutfitUtilities.get_ts4_outfit_category(outfit_category)
        outfit_cat_and_idx: Tuple[OutfitCategory, int] = (outfit_category, outfit_index)
        if not CommonOutfitUtils.has_outfit(sim_info, outfit_cat_and_idx):
            sim_info.get_outfit(outfit_cat_and_idx[0], outfit_cat_and_idx[1])  # generate outfit
        sim_outfit_io = CommonSimOutfitIO(sim_info, outfit_category_and_index=outfit_cat_and_idx, initial_outfit_parts=parts, mod_identity=ModInfo.get_identity())
        sim_outfit_io.apply(resend_outfits_after_apply=True, apply_to_outfit_category_and_index=outfit_cat_and_idx)
        sim_info.on_outfit_generated(*outfit_cat_and_idx)
        sim_info.set_outfit_dirty(outfit_cat_and_idx[0])
        sim_info.set_current_outfit(outfit_cat_and_idx)

    # outfit_utils.py#def get_maximum_outfits_for_category(outfit_category):
    @staticmethod
    def get_maximum_outfits_for_category(outfit_category: Union[CustomOutfitCategory, OutfitCategory, int, str]):
        outfit_category: CustomOutfitCategory = OutfitUtilities.get_ts4_outfit_category(outfit_category)
        if outfit_category in [OutfitCategory.BATHING, OutfitCategory.SITUATION, ]:
            return 1
        elif outfit_category in [OutfitCategory.SPECIAL, OutfitCategory.CAREER, ]:
            return 3
        return 5
        # return get_maximum_outfits_for_category(outfit_category)

    @staticmethod
    def get_ts4_outfit_category(outfit_category: Union[CustomOutfitCategory, OutfitCategory, int]):
        if isinstance(outfit_category, int):
            outfit_category = OutfitCategory(outfit_category)
        elif isinstance(outfit_category, CustomOutfitCategory):
            outfit_category = OutfitCategory(outfit_category.value)
        return outfit_category

    @staticmethod
    def get_custom_outfit_category(outfit_category: Union[CustomOutfitCategory, OutfitCategory, int, str]):
        if isinstance(outfit_category, int) or isinstance(outfit_category, OutfitCategory):
            outfit_category = CustomOutfitCategory(outfit_category)
        elif isinstance(outfit_category, str):
            outfit_category = CustomOutfitCategory[outfit_category]
        return outfit_category