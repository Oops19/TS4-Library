#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class SimRegion(CustomEnum):
    """ As used by sliders / MorphMaker """
    INVALID = -1
    EYES = 0
    NOSE = 1
    MOUTH = 2
    CHEEKS = 3
    CHIN = 4
    JAW = 5
    FOREHEAD = 6

    BROWS = 8
    EARS = 9
    HEAD = 10

    FULLFACE = 12

    CHEST = 14
    UPPERCHEST = 15

    NECK = 16
    SHOULDERS = 17
    UPPERARM = 18
    LOWERARM = 19
    HANDS = 20
    WAIST = 21
    HIPS = 22
    BELLY = 23
    BUTT = 24
    THIGHS = 2
    LOWERLEG = 26
    FEET = 27

    BODY = 28
    UPPERBODY = 29
    LOWERBODY = 30
    TAIL = 31
    FUR = 32
    FORELEGS = 33
    HINDLEGS = 34

    CUSTOM_MALE_PARTS = 50
    CUSTOM_FEMALE_PARTS = 51
    CUSTOM_BREASTS = 52
    CUSTOM_CHEST = 53
    CUSTOM_UPPER_CHEST = 54
    CUSTOM_BACK = 55
    CUSTOM_NECK = 56
    CUSTOM_SHOULDERS = 57
    CUSTOM_UPPER_ARM = 58
    CUSTOM_LOWER_ARM = 59
    CUSTOM_HANDS = 60
    CUSTOM_WAIST = 61
    CUSTOM_HIPS = 62
    CUSTOM_BELLY = 63
    CUSTOM_BUTT = 64
    CUSTOM_THIGHS = 65
    CUSTOM_LOWER_LEG = 66
    CUSTOM_FETT = 67
    CUSTOM_MISC_1 = 68
    CUSTOM_MISC_2 = 69
    CUSTOM_MISC_3 = 70
    CUSTOM_MISC_4 = 71
    CUSTOM_MISC_5 = 72
