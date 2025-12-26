#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomSpecies(CustomEnum):
    INVALID: 'CustomSpecies' = 0
    HUMAN: 'CustomSpecies' = 1
    DOG: 'CustomSpecies' = 2  # CHILD or ADULT
    CAT: 'CustomSpecies' = 3  # CHILD or ADULT
    SMALL_DOG: 'CustomSpecies' = 4  # ADULT
    SMALLDOG: 'CustomSpecies' = 4  # TS4 name
    FOX: 'CustomSpecies' = 5  # ADULT
    HORSE: 'CustomSpecies' = 6

    ANIMAL: 'CustomSpecies' = 253  # S4CL name, custom value
    LARGE_DOG: 'CustomSpecies' = 254  # S4CL name, custom value
    PET: 'CustomSpecies' = 255  # S4CL name, custom value
