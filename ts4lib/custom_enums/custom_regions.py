#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomRegions(CustomEnum):
    """ Identifiers for vanilla 'regions'. """

    INVALID: 'CustomRegions' = 0
    BGDEBUG_MEGA_LOTS_TEST_WORLD: 'CustomRegions' = 131195
    CAREER_ALIEN_WORLD: 'CustomRegions' = 108705
    CAREER_DOCTOR_CLINIC: 'CustomRegions' = 109306
    CAREER_POLICE_STATION: 'CustomRegions' = 108706
    CAREER_RETAIL: 'CustomRegions' = 108704
    CAREER_SCIENCE_LAB: 'CustomRegions' = 108707
    DEBUG_EP07_TEST_WORLD: 'CustomRegions' = 197994
    DEBUG_MAGALOG: 'CustomRegions' = 104067
    DEBUG_PERF_TEST: 'CustomRegions' = 104068
    DEBUG_TEST_WORLD: 'CustomRegions' = 104066
    DEBUG_TEST_WORLD_GP02: 'CustomRegions' = 121398
    DESTINATION_BATUU: 'CustomRegions' = 231104
    DESTINATION_CAMPING_FOREST: 'CustomRegions' = 104096
    DESTINATION_JUNGLE: 'CustomRegions' = 173593
    HIDDEN_ACTING_STUDIO: 'CustomRegions' = 190064
    HIDDEN_FORGOTTEN_GROTTO: 'CustomRegions' = 104062
    HIDDEN_MAGIC_VENUE: 'CustomRegions' = 219134
    HIDDEN_SYLVAN_GLADE: 'CustomRegions' = 104063
    RESIDENTIAL_BAY_AREA: 'CustomRegions' = 302872
    RESIDENTIAL_CITY_LIFE: 'CustomRegions' = 134252
    RESIDENTIAL_COTTAGE_WORLD: 'CustomRegions' = 257397
    RESIDENTIAL_ECO_WORLD: 'CustomRegions' = 228200
    RESIDENTIAL_EP14WORLD: 'CustomRegions' = 311185
    RESIDENTIAL_EP16WORLD: 'CustomRegions' = 362425
    RESIDENTIAL_FAME_WORLD: 'CustomRegions' = 195493
    RESIDENTIAL_HIGH_SCHOOL_WORLD: 'CustomRegions' = 272365
    RESIDENTIAL_ISLAND_WORLD: 'CustomRegions' = 208308
    RESIDENTIAL_MAGIC: 'CustomRegions' = 216626
    RESIDENTIAL_MOUNTAIN_WORLD: 'CustomRegions' = 238454
    RESIDENTIAL_MULTI_UNIT_WORLD: 'CustomRegions' = 337554
    RESIDENTIAL_NEWCREST: 'CustomRegions' = 119917
    RESIDENTIAL_NORTH_EUROPE: 'CustomRegions' = 123129
    RESIDENTIAL_OASIS_SPRINGS: 'CustomRegions' = 104065
    RESIDENTIAL_PET_WORLD: 'CustomRegions' = 166547
    RESIDENTIAL_STRANGETOWN: 'CustomRegions' = 201699
    RESIDENTIAL_UNIVERSITY_WORLD: 'CustomRegions' = 208814
    RESIDENTIAL_VAMPIRE_WORLD: 'CustomRegions' = 152175
    RESIDENTIAL_WEDDING_WORLD: 'CustomRegions' = 272129
    RESIDENTIAL_WILLOW_CREEK: 'CustomRegions' = 104064
    RESIDENTIAL_WOLF_TOWN: 'CustomRegions' = 285909

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID
