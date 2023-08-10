
#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class VanillaBlocks(CommonEnum):
    """ Identifiers for vanilla 'venues'. """

    INVALID: 'VanillaBlocks' = -1
    OUTSIDE: 'VanillaBlocks' = 0
    INSIDE: 'VanillaBlocks' = 2 ** 32  # Inside is set to a valid block_id which is likely unused.

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID
