#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class OccultType(CommonEnum):
    INVALID: 'OccultType' = 0
    HUMAN: 'OccultType' = 1
    ALIEN: 'OccultType' = 2
    VAMPIRE: 'OccultType' = 4
    MERMAID: 'OccultType' = 8
    WITCH: 'OccultType' = 16
    WEREWOLF: 'OccultType' = 32
    FAIRY: 'OccultType' = 64
    # Future use 64 = 2 ** 16
    # Future use 128 = 2 ** 17
    # Future use 256 = 2 ** 18
    # These are not TS4 occults
    GHOST: 'OccultType' = 2 ** 19
    ROBOT: 'OccultType' = 2 ** 20
    SCARECROW: 'OccultType' = 2 ** 21
    SKELETON: 'OccultType' = 2 ** 22
    PLANT_SIM: 'OccultType' = 2 ** 23
