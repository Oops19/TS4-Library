#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class Species(CommonEnum):
    INVALID: 'Species' = 0
    HUMAN: 'Species' = 1
    DOG: 'Species' = 2  # CHILD or ADULT
    CAT: 'Species' = 3  # CHILD or ADULT
    SMALL_DOG: 'Species' = 4  # ADULT
    SMALLDOG: 'Species' = 4  # TS4 name
    FOX: 'Species' = 5  # ADULT
    HORSE: 'Species' = 6

    ANIMAL: 'Species' = 253  # S4CL name, custom value
    LARGE_DOG: 'Species' = 254  # S4CL name, custom value
    PET: 'Species' = 255  # S4CL name, custom value
