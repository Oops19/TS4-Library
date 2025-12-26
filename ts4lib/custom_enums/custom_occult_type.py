#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomOccultType(CustomEnum):
    INVALID: 'CustomOccultType' = 0
    HUMAN: 'CustomOccultType' = 1
    ALIEN: 'CustomOccultType' = 2
    VAMPIRE: 'CustomOccultType' = 4
    MERMAID: 'CustomOccultType' = 8
    WITCH: 'CustomOccultType' = 16
    WEREWOLF: 'CustomOccultType' = 32
    FAIRY: 'CustomOccultType' = 64
    # Future use 64 = 2 ** 16
    # Future use 128 = 2 ** 17
    # Future use 256 = 2 ** 18
    # These are not TS4 occults
    GHOST: 'CustomOccultType' = 2 ** 19
    ROBOT: 'CustomOccultType' = 2 ** 20
    SCARECROW: 'CustomOccultType' = 2 ** 21
    SKELETON: 'CustomOccultType' = 2 ** 22
    PLANT_SIM: 'CustomOccultType' = 2 ** 23
