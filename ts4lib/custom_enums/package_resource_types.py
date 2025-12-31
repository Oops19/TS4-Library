#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


from ts4lib.custom_enums.custom_resource_type import CustomResourceType
from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class PackageResourceTypes(CustomEnum):
    """
    Grouped resource types as lists to be used by the mod.
    This is the place to modify the defaults for this mod.
    To add a new CustomResourceType add it first in the CustomResourceType class and then reference it here.
    """
    STBLS = {CustomResourceType.STBL.value, }
    DATAS = {CustomResourceType.CAS_PART.value, }
    NAMES = {CustomResourceType.CAS_PART.value, CustomResourceType.OBJECT_DEFINITION.value, }
    SLIDERS = {CustomResourceType.SCULPT.value, CustomResourceType.SIM_MODIFIER.value, CustomResourceType.DEFORMER_MAP.value, }
    RIGS = {CustomResourceType.RIG.value, }

    EA_TUNINGS = {
        CustomResourceType.TUNING.value,
        CustomResourceType.TUNING_TRAIT.value,
        CustomResourceType.TUNING_BUFF.value,
        CustomResourceType.TUNING_SUPER_INTERACTION.value,
        CustomResourceType.TUNING_ANIMATION_ELEMENT.value,
        CustomResourceType.TUNING_AWAY_ACTION.value,
        CustomResourceType.TUNING_BALLOON_CATEGORY.value,
        CustomResourceType.TUNING_BROADCASTER.value,
        CustomResourceType.TUNING_BUCKS_PERK.value,
        CustomResourceType.TUNING_CAREER.value,
        CustomResourceType.TUNING_CAREER_LEVEL.value,
        CustomResourceType.TUNING_GAME_OBJECT.value,
        CustomResourceType.TUNING_GAME_RULES.value,
        CustomResourceType.TUNING_LOOT_ACTIONS.value,
        CustomResourceType.TUNING_MOOD.value,
        CustomResourceType.TUNING_NPC_INVITE_SITUATION_DRAMA_NODE.value,
        CustomResourceType.TUNING_OBJECT_STATE.value,
        CustomResourceType.TUNING_OBJECTIVE.value,
        CustomResourceType.TUNING_OBJECTIVELESS_WHIM_SET.value,
        CustomResourceType.TUNING_PIE_MENU_CATEGORY.value,
        CustomResourceType.TUNING_RABBIT_HOLE.value,
        CustomResourceType.TUNING_RECIPE.value,
        CustomResourceType.TUNING_RELATIONSHIP_BIT.value,
        CustomResourceType.TUNING_ROLE_STATE.value,
        CustomResourceType.TUNING_SIM_REWARD.value,
        CustomResourceType.TUNING_SITUATION_GOAL_RAN_INTERACTION_ON_TARGETED_SIM.value,
        CustomResourceType.TUNING_SITUATION_GOAL_SET.value,
        CustomResourceType.TUNING_SITUATION_JOB.value,
        CustomResourceType.TUNING_SITUATION_SIMPLE.value,
        CustomResourceType.TUNING_SLOT_TYPE.value,
        CustomResourceType.TUNING_SNIPPET.value,
        CustomResourceType.TUNING_SOCIAL_GROUP.value,
        CustomResourceType.TUNING_STATIC_COMMODITY.value,
        CustomResourceType.TUNING_STATISTIC.value,
        CustomResourceType.TUNING_TUNABLE_CAREER_TRACK.value,
        CustomResourceType.TUNING_TUNABLE_SIM_FILTER.value,
        CustomResourceType.TUNING_TUNABLE_SIM_TEMPLATE.value,
        CustomResourceType.TUNING_TUNABLE_TAG_SET.value,
        CustomResourceType.TUNING_TUNABLE_TEMPLATE_CHOOSER.value,
        CustomResourceType.TUNING_TUTORIAL_CATEGORY.value,
        CustomResourceType.TUNING_ZONE_MODIFIER.value,
        CustomResourceType.TUNING_ZONE_MODIFIER_DISPLAY_INFO.value,
    }
    UGC_TUNINGS = set()
    EA_XML = {
        CustomResourceType.ANIMATION_STATE_MACHINE.value,
        CustomResourceType.WIDGET_LIST.value,
        CustomResourceType.XML_ASM.value,
        CustomResourceType.XML_LOT_TYPE_EVENT_MAPS.value,
        CustomResourceType.XML_PROP_X.value,
        CustomResourceType.XML_MODAL_MUSIC_MAPPING.value,
        CustomResourceType.XML_CREDITS.value,
        CustomResourceType.XML_UI_EVENT_MODE_MAPPINGS.value,
        CustomResourceType.XML_EFFECT.value,
        CustomResourceType.XML_PREFIX_SUFFIX_MAPPING.value,
        CustomResourceType.XML_LOCOMOTION_ANIMATION.value,
        CustomResourceType.XML_AMBIENCE.value,
        CustomResourceType.XML_VOICE.value,
        CustomResourceType.XML_MUSIC_DATA.value,
    }
    UGC_XML = {
        CustomResourceType.S4S_BATCH_FIX.value,

    }
    TUNINGS = EA_TUNINGS | UGC_TUNINGS
    XML = EA_XML | UGC_XML
    TUNINGS_AND_XML = TUNINGS | XML

    PNG_IMAGES = {
        # image format might be JPG or DST in UGC
        CustomResourceType.IMAGE_PNG_CAS_PART_THUMBNAIL.value,
        CustomResourceType.IMAGE_PNG_CAS_BUILD_THUMBNAIL.value,
        CustomResourceType.IMAGE_PNG_1.value,
        CustomResourceType.IMAGE_PNG_2.value,
        CustomResourceType.IMAGE_PNG_3.value,
        CustomResourceType.IMAGE_PNG_4.value,
        CustomResourceType.IMAGE_PNG_5.value,
        CustomResourceType.IMAGE_PNG_6.value,
        CustomResourceType.IMAGE_PNG_7.value,
        CustomResourceType.IMAGE_PNG_8.value,

    }
    OTHER_IMAGES = {
        CustomResourceType.IMAGE_DST.value,
        CustomResourceType.IMAGE_RLE_2.value,
        CustomResourceType.IMAGE_RLES.value,

    }
    IMAGES = PNG_IMAGES | OTHER_IMAGES