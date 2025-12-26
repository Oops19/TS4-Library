#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomAge(CustomEnum):
    NONE: 'CustomAge' = 0
    INVALID: 'CustomAge' = 0
    BABY: 'CustomAge' = 1
    TODDLER: 'CustomAge' = 2
    CHILD: 'CustomAge' = 4
    TEEN: 'CustomAge' = 8
    YOUNG_ADULT: 'CustomAge' = 16
    YOUNGADULT: 'CustomAge' = 16  # TS4 name
    ADULT: 'CustomAge' = 32
    ELDER: 'CustomAge' = 64
    INFANT: 'CustomAge' = 128
