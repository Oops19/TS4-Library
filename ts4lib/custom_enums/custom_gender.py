#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomGender(CustomEnum):
    NONE: 'CustomGender' = 0
    INVALID: 'CustomGender' = 0
    MALE: 'CustomGender' = 4096
    FEMALE: 'CustomGender' = 8192

    # This value might change in future, not official
    UNISEX: 'CustomGender' = 4096 + 8192