#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class VanillaNames:
    """ Class to return 'Foo Bar' for enum <EnumName.FOO_BAR: 1> """
    @staticmethod
    def get(enum: CommonEnum):
        return enum.name.title().replace('_', ' ')
