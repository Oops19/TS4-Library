
#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class VanillaVenues(CommonEnum):
    """ Identifiers for vanilla 'venues'. """

    INVALID: 'VanillaVenues' = 0
    ACTING_STUDIO: 'VanillaVenues' = 190058
    ARTSCENTER: 'VanillaVenues' = 144206
    AUDITORIUM: 'VanillaVenues' = 281069
    AUDITORIUM_CAREER_DAY: 'VanillaVenues' = 292915
    AUDITORIUM_FORMAL_DANCE: 'VanillaVenues' = 281068
    AUDITORIUM_GRADUATION: 'VanillaVenues' = 281066
    BAR: 'VanillaVenues' = 16869
    BEACH: 'VanillaVenues' = 205126
    CAFE: 'VanillaVenues' = 122247
    CHALET_GARDENS: 'VanillaVenues' = 125223
    CLUB: 'VanillaVenues' = 16870
    COMMUNITY_LOT: 'VanillaVenues' = 223944
    DOCTOR_CLINIC: 'VanillaVenues' = 110576
    FIRST_ORDER_OUTPOST: 'VanillaVenues' = 231964
    FOREST_PARK: 'VanillaVenues' = 107453
    GARDEN: 'VanillaVenues' = 223946
    GENERIC: 'VanillaVenues' = 9279
    GYM: 'VanillaVenues' = 16873
    HERMIT: 'VanillaVenues' = 105591
    HIDDEN_ALIEN_WORLD: 'VanillaVenues' = 111611
    HIDDEN_CAVE: 'VanillaVenues' = 98133
    HIDDEN_GLADE: 'VanillaVenues' = 98132
    HIGH_SCHOOL: 'VanillaVenues' = 278305
    KARAOKE: 'VanillaVenues' = 137844
    LIBRARY: 'VanillaVenues' = 16874
    LOUNGE: 'VanillaVenues' = 16875
    MAGIC_HQ: 'VanillaVenues' = 212896
    MAKER_SPACE: 'VanillaVenues' = 231465
    MARKET: 'VanillaVenues' = 223945
    MOUNTAIN_EXCURSION: 'VanillaVenues' = 247118
    MUSEUM: 'VanillaVenues' = 16876
    MYSHUNO_MEADOWS: 'VanillaVenues' = 138380
    NATURAL_POOL: 'VanillaVenues' = 175123
    OCEAN_BLUFF: 'VanillaVenues' = 125071
    OGAS_CANTINA: 'VanillaVenues' = 233449
    ONSEN: 'VanillaVenues' = 247473
    PARK: 'VanillaVenues' = 25847
    PENTHOUSE: 'VanillaVenues' = 149495
    POLICE_STATION: 'VanillaVenues' = 109774
    POOL: 'VanillaVenues' = 123794
    RELAXATION_CENTER: 'VanillaVenues' = 118135
    RENTABLE_CABIN: 'VanillaVenues' = 103675
    RENTABLE_JUNGLE: 'VanillaVenues' = 173833
    RENTABLE_UNIVERSITY_HOUSING: 'VanillaVenues' = 208182
    RENTABLE_VACATION_GENERIC: 'VanillaVenues' = 239458
    RESIDENTIAL: 'VanillaVenues' = 28614
    RESIDENTIAL_TINYHOME: 'VanillaVenues' = 229251
    RESISTANCE_CAMP: 'VanillaVenues' = 231965
    RESTAURANT: 'VanillaVenues' = 130713
    RETAIL: 'VanillaVenues' = 105157
    RUINS: 'VanillaVenues' = 123132
    SCIENTIST_LAB: 'VanillaVenues' = 107487
    SECRET_LAB: 'VanillaVenues' = 202003
    TEMPLE: 'VanillaVenues' = 173492
    THRIFT_STORE: 'VanillaVenues' = 278997
    UNIVERSITY_STUDENT_COMMONS_ARTS: 'VanillaVenues' = 218857
    UNIVERSITY_STUDENT_COMMONS_SCIENCE: 'VanillaVenues' = 218858
    VET: 'VanillaVenues' = 158847
    VISITORS_ALLOWED: 'VanillaVenues' = 98817
    WEDDING: 'VanillaVenues' = 273016

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID
