
#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023-2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomBlocks(CustomEnum):
    """ Identifiers for vanilla 'venues'. """

    INVALID: 'CustomBlocks' = -1
    OUTSIDE: 'CustomBlocks' = 0
    INSIDE: 'CustomBlocks' = 2 ** 32  # Inside is set to a valid block_id which is likely unused.

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID
