#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomIntEnum


class CustomOutfitIndex(CustomIntEnum):
    NONE: 'CustomOutfitIndex' = -1
    DEFAULT: 'CustomOutfitIndex' = 0
    OPTION_1: 'CustomOutfitIndex' = 1
    OPTION_2: 'CustomOutfitIndex' = 2
    OPTION_3: 'CustomOutfitIndex' = 3
    OPTION_4: 'CustomOutfitIndex' = 4
    # For CustomOutfitCategory.SPECIAL
    SPECIAL_TOWEL: 'CustomOutfitIndex' = 1
    SPECIAL_FASHION: 'CustomOutfitIndex' = 2

