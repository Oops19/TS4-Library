
#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#

from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class VanillaRegions(CommonEnum):
    """ Identifiers for vanilla 'regions'. """

    INVALID: 'VanillaRegions' = 0
    BGDEBUG_MEGA_LOTS_TEST_WORLD: 'VanillaRegions' = 131195
    CAREER_ALIEN_WORLD: 'VanillaRegions' = 108705
    CAREER_DOCTOR_CLINIC: 'VanillaRegions' = 109306
    CAREER_POLICE_STATION: 'VanillaRegions' = 108706
    CAREER_RETAIL: 'VanillaRegions' = 108704
    CAREER_SCIENCE_LAB: 'VanillaRegions' = 108707
    DEBUG_EP07_TEST_WORLD: 'VanillaRegions' = 197994
    DEBUG_MAGALOG: 'VanillaRegions' = 104067
    DEBUG_PERF_TEST: 'VanillaRegions' = 104068
    DEBUG_TEST_WORLD: 'VanillaRegions' = 104066
    DEBUG_TEST_WORLD_GP02: 'VanillaRegions' = 121398
    DESTINATION_BATUU: 'VanillaRegions' = 231104
    DESTINATION_CAMPING_FOREST: 'VanillaRegions' = 104096
    DESTINATION_JUNGLE: 'VanillaRegions' = 173593
    HIDDEN_ACTING_STUDIO: 'VanillaRegions' = 190064
    HIDDEN_FORGOTTEN_GROTTO: 'VanillaRegions' = 104062
    HIDDEN_MAGIC_VENUE: 'VanillaRegions' = 219134
    HIDDEN_SLYVAN_GLADE: 'VanillaRegions' = 104063
    RESIDENTIAL_CITY_LIFE: 'VanillaRegions' = 134252
    RESIDENTIAL_COTTAGE_WORLD: 'VanillaRegions' = 257397
    RESIDENTIAL_ECO_WORLD: 'VanillaRegions' = 228200
    RESIDENTIAL_FAME_WORLD: 'VanillaRegions' = 195493
    RESIDENTIAL_HIGH_SCHOOL_WORLD: 'VanillaRegions' = 272365
    RESIDENTIAL_ISLAND_WORLD: 'VanillaRegions' = 208308
    RESIDENTIAL_MAGIC: 'VanillaRegions' = 216626
    RESIDENTIAL_MOUNTAIN_WORLD: 'VanillaRegions' = 238454
    RESIDENTIAL_NEWCREST: 'VanillaRegions' = 119917
    RESIDENTIAL_NORTH_EUROPE: 'VanillaRegions' = 123129
    RESIDENTIAL_OASIS_SPRINGS: 'VanillaRegions' = 104065
    RESIDENTIAL_PET_WORLD: 'VanillaRegions' = 166547
    RESIDENTIAL_STRANGETOWN: 'VanillaRegions' = 201699
    RESIDENTIAL_UNIVERSITY_WORLD: 'VanillaRegions' = 208814
    RESIDENTIAL_VAMPIRE_WORLD: 'VanillaRegions' = 152175
    RESIDENTIAL_WILLOW_CREEK: 'VanillaRegions' = 104064

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID
