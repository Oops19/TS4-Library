#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class Age(CommonEnum):
    NONE: 'Age' = 0
    INVALID: 'Age' = 0
    BABY: 'Age' = 1
    TODDLER: 'Age' = 2
    CHILD: 'Age' = 4
    TEEN: 'Age' = 8
    YOUNG_ADULT: 'Age' = 16
    YOUNGADULT: 'Age' = 16  # TS4 name
    ADULT: 'Age' = 32
    ELDER: 'Age' = 64
    INFANT: 'Age' = 128
