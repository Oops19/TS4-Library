#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomVenues(CustomEnum):
    """ Identifiers for vanilla 'venues'. """

    INVALID: 'CustomVenues' = 0
    ACTING_STUDIO: 'CustomVenues' = 190058
    ARTSCENTER: 'CustomVenues' = 144206
    AUDITORIUM: 'CustomVenues' = 281069
    AUDITORIUM_CAREER_DAY: 'CustomVenues' = 292915
    AUDITORIUM_FORMAL_DANCE: 'CustomVenues' = 281068
    AUDITORIUM_GRADUATION: 'CustomVenues' = 281066
    BAR: 'CustomVenues' = 16869
    BEACH: 'CustomVenues' = 205126
    CAFE: 'CustomVenues' = 122247
    CHALET_GARDENS: 'CustomVenues' = 125223
    CLUB: 'CustomVenues' = 16870
    COMMUNITY_LOT: 'CustomVenues' = 223944
    DOCTOR_CLINIC: 'CustomVenues' = 110576
    FIRST_ORDER_OUTPOST: 'CustomVenues' = 231964
    FOREST_PARK: 'CustomVenues' = 107453
    GARDEN: 'CustomVenues' = 223946
    GENERIC: 'CustomVenues' = 9279
    GYM: 'CustomVenues' = 16873
    HERMIT: 'CustomVenues' = 105591
    HIDDEN_ALIEN_WORLD: 'CustomVenues' = 111611
    HIDDEN_CAVE: 'CustomVenues' = 98133
    HIDDEN_GLADE: 'CustomVenues' = 98132
    HIGH_SCHOOL: 'CustomVenues' = 278305
    KARAOKE: 'CustomVenues' = 137844
    LIBRARY: 'CustomVenues' = 16874
    LOUNGE: 'CustomVenues' = 16875
    MAGIC_HQ: 'CustomVenues' = 212896
    MAKER_SPACE: 'CustomVenues' = 231465
    MARKET: 'CustomVenues' = 223945
    MOUNTAIN_EXCURSION: 'CustomVenues' = 247118
    MUSEUM: 'CustomVenues' = 16876
    MYSHUNO_MEADOWS: 'CustomVenues' = 138380
    NATURAL_POOL: 'CustomVenues' = 175123
    OCEAN_BLUFF: 'CustomVenues' = 125071
    OGAS_CANTINA: 'CustomVenues' = 233449
    ONSEN: 'CustomVenues' = 247473
    PARK: 'CustomVenues' = 25847
    PENTHOUSE: 'CustomVenues' = 149495
    POLICE_STATION: 'CustomVenues' = 109774
    POOL: 'CustomVenues' = 123794
    RELAXATION_CENTER: 'CustomVenues' = 118135
    RENTABLE_CABIN: 'CustomVenues' = 103675
    RENTABLE_JUNGLE: 'CustomVenues' = 173833
    RENTABLE_UNIVERSITY_HOUSING: 'CustomVenues' = 208182
    RENTABLE_VACATION_GENERIC: 'CustomVenues' = 239458
    RESIDENTIAL: 'CustomVenues' = 28614
    RESIDENTIAL_TINYHOME: 'CustomVenues' = 229251
    RESISTANCE_CAMP: 'CustomVenues' = 231965
    RESTAURANT: 'CustomVenues' = 130713
    RETAIL: 'CustomVenues' = 105157
    RUINS: 'CustomVenues' = 123132
    SCIENTIST_LAB: 'CustomVenues' = 107487
    SECRET_LAB: 'CustomVenues' = 202003
    TEMPLE: 'CustomVenues' = 173492
    THRIFT_STORE: 'CustomVenues' = 278997
    UNIVERSITY_STUDENT_COMMONS_ARTS: 'CustomVenues' = 218857
    UNIVERSITY_STUDENT_COMMONS_SCIENCE: 'CustomVenues' = 218858
    VET: 'CustomVenues' = 158847
    VISITORS_ALLOWED: 'CustomVenues' = 98817
    WEDDING: 'CustomVenues' = 273016

    @classmethod
    def _missing_(cls, value):
        return cls.INVALID
