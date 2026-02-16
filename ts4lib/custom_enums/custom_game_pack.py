#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#

# https://sims4.crinrict.com/eng/extras-2/available-packs-dlc/

# noinspection PyUnresolvedReferences
import _common_types
from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class CustomGamePack(CustomEnum):
    try:
        NONE: 'CustomGamePack' = None

        BASE_GAME: 'CustomGamePack' = _common_types.BASE_GAME  # 0
        FP01_HOLIDAY_CELEBRATIONS: 'CustomGamePack' = _common_types.FP01  # 5

        EP01_GET_TO_WORK: 'CustomGamePack' = _common_types.EP01  # 3
        EP02_GET_TOGETHER: 'CustomGamePack' = _common_types.EP02  # 9
        EP03_CITY_LIVING: 'CustomGamePack' = _common_types.EP03  # 24
        EP04_CATS_AND_DOGS: 'CustomGamePack' = _common_types.EP04  # 25
        EP05_SEASONS: 'CustomGamePack' = _common_types.EP05  # 26
        EP06_GET_FAMOUS: 'CustomGamePack' = _common_types.EP06  # 27
        EP07_ISLAND_LIVING: 'CustomGamePack' = _common_types.EP07  # 28
        EP08_DISCOVER_UNIVERSITY: 'CustomGamePack' = _common_types.EP08  # 29
        EP09_ECO_LIFESTYLE: 'CustomGamePack' = _common_types.EP09  # 30
        EP10_SNOWY_ESCAPE: 'CustomGamePack' = _common_types.EP10  # 31
        EP11_COTTAGE_LIVING: 'CustomGamePack' = _common_types.EP11  # 52
        EP12_HIGH_SCHOOL_YEARS: 'CustomGamePack' = _common_types.EP12  # 53 2022-07-28
        EP13_GROWING_TOGETHER: 'CustomGamePack' = _common_types.EP13  # 54
        EP14_HORSE_RANCH: 'CustomGamePack' = _common_types.EP14  # 55
        EP15_FOR_RENT: 'CustomGamePack' = _common_types.EP15  # 56
        EP16_LOVESTRUCK: 'CustomGamePack' = _common_types.EP16  # 57 2024-07-25
        EP17_LIFE_AND_DEATH: 'CustomGamePack' = _common_types.EP17  # 58 2024-10-31
        EP18_BUSINESS_AND_HOBBIES: 'CustomGamePack' = _common_types.EP18  # 59 2025-03-06
        EP19_ENCHANTED_BY_NATURE: 'CustomGamePack' = _common_types.EP19  # 60 2025-07-10 ---
        EP20_ADVENTURE_AWAITS: 'CustomGamePack' = _common_types.EP20   # 61 2025-10-02 ---
        EP21_ROYALTY_AND_LEGACY: 'CustomGamePack' = _common_types.EP21   # 141 2026-02-12 ---
        EP22: 'CustomGamePack' = _common_types.EP22  # 142 2026-tbd
        # ... EP29 = 149; EP30 = 256 ... EP49 = 275

        GP01_OUTDOOR_RETREAT: 'CustomGamePack' = _common_types.GP01  # 2
        GP02_SPA_DAY: 'CustomGamePack' = _common_types.GP02  # 6
        GP03_DINE_OUT: 'CustomGamePack' = _common_types.GP03   # 10
        GP04_VAMPIRES: 'CustomGamePack' = _common_types.GP04  # 17
        GP05_PARENTHOOD: 'CustomGamePack' = _common_types.GP05  # 18
        GP06_JUNGLE_ADVENTURES: 'CustomGamePack' = _common_types.GP06  # 19
        GP07_STRANGERVILLE: 'CustomGamePack' = _common_types.GP07  # 20
        GP08_REALM_OF_MAGIC: 'CustomGamePack' = _common_types.GP08  # 21
        GP09_STAR_WARS_JOURNEY_TO_BATUU: 'CustomGamePack' = _common_types.GP09  # 22
        GP10_DREAM_HOME_DECORATOR: 'CustomGamePack' = _common_types.GP10  # 23
        GP11_MY_WEDDING_STORIES: 'CustomGamePack' = _common_types.GP11  # 62
        GP12_WEREWOLVES: 'CustomGamePack' = _common_types.GP12  # 63
        GP13: 'CustomGamePack' = _common_types.GP13  # 64 2026-tbd
        # ... GP20 = 71; GP21 = 756 ... GP40 = 775

        SP01_LUXURY_PARTY: 'CustomGamePack' = _common_types.SP01  # 1
        SP02_PERFECT_PATIO: 'CustomGamePack' = _common_types.SP02  # 4
        SP03_COOL_KITCHEN: 'CustomGamePack' = _common_types.SP03  # 7
        SP04_SPOOKY: 'CustomGamePack' = _common_types.SP04  # 8
        SP05_MOVIE_HANGOUT: 'CustomGamePack' = _common_types.SP05  # 11
        SP06_ROMANTIC_GARDEN: 'CustomGamePack' = _common_types.SP06  # 12
        SP07_KIDS_ROOM: 'CustomGamePack' = _common_types.SP07  # 13
        SP08_BACKYARD: 'CustomGamePack' = _common_types.SP08  # 14
        SP09_VINTAGE_GLAMOUR: 'CustomGamePack' = _common_types.SP09  # 15
        SP10_BOWLING_NIGHT: 'CustomGamePack' = _common_types.SP10  # 16
        SP11_FITNESS: 'CustomGamePack' = _common_types.SP11  # 32
        SP12_TODDLER: 'CustomGamePack' = _common_types.SP12  # 33
        SP13_LAUNDRY_DAY: 'CustomGamePack' = _common_types.SP13  # 34
        SP14_MY_FIRST_PET: 'CustomGamePack' = _common_types.SP14  # 35
        SP15_MOSCHINO: 'CustomGamePack' = _common_types.SP15  # 36
        SP16_TINY_LIVING: 'CustomGamePack' = _common_types.SP16  # 37
        SP17_NIFTY_KNITTING: 'CustomGamePack' = _common_types.SP17  # 38
        SP18_PARANORMAL: 'CustomGamePack' = _common_types.SP18  # 39 2023-01-26
        SP46_HOME_CHEF_HUSTLE: 'CustomGamePack' = _common_types.SP46  # 87 2023-09-28 ---
        SP49_CRYSTAL_CREATIONS: 'CustomGamePack' = _common_types.SP49  # 90 2024-02-29

        # Build Kits
        SP21_COUNTRY_KITCHEN: 'CustomGamePack' = _common_types.SP21  #
        SP23_COURTYARD_OASIS: 'CustomGamePack' = _common_types.SP23  #
        SP25_INDUSTRIAL_LOFT: 'CustomGamePack' = _common_types.SP25  #
        SP29_BLOOMING_ROOMS: 'CustomGamePack' = _common_types.SP29  #
        SP31_DECOR_TO_THE_MAX: 'CustomGamePack' = _common_types.SP31  #
        SP33_LITTLE_CAMPERS: 'CustomGamePack' = _common_types.SP33  #
        SP35_DESERT_LUXE: 'CustomGamePack' = _common_types.SP35  #
        SP36_PASTEL_POP: 'CustomGamePack' = _common_types.SP36  #
        SP37_EVERYDAY_CLUTTER: 'CustomGamePack' = _common_types.SP37  #
        SP39_BATHROOM_CLUTTER: 'CustomGamePack' = _common_types.SP39  #
        SP40_GREENHOUSE_HAVEN: 'CustomGamePack' = _common_types.SP40  #
        SP41_BASEMENT_TREASURES: 'CustomGamePack' = _common_types.SP41  #
        SP43_BOOK_NOOK: 'CustomGamePack' = _common_types.SP43  #
        SP45_MODERN_LUXE: 'CustomGamePack' = _common_types.SP45  #
        SP47_CASTLE_ESTATE: 'CustomGamePack' = _common_types.SP47  #
        SP51_PARTY_ESSENTIALS: 'CustomGamePack' = _common_types.SP51  #
        SP52_RIVIERA_RETREAT: 'CustomGamePack' = _common_types.SP52  #
        SP53_COZY_BISTRO: 'CustomGamePack' = _common_types.SP53  #
        SP54_ARTIST_STUDIO: 'CustomGamePack' = _common_types.SP54  #
        SP55_STORYBOOK_NURSERY: 'CustomGamePack' = _common_types.SP55  #
        SP57_COZY_KITSCH: 'CustomGamePack' = _common_types.SP57  #
        SP58_COMFY_GAMER: 'CustomGamePack' = _common_types.SP58  #
        SP61_REFINED_LIVING_ROOM: 'CustomGamePack' = _common_types.SP61  #
        SP63_SLEEK_BATHROOM: 'CustomGamePack' = _common_types.SP63  #
        SP65_RESTORATION_WORKSHOP: 'CustomGamePack' = _common_types.SP65  #
        SP67_KITCHEN_CLUTTER: 'CustomGamePack' = _common_types.SP67  #
        SP68_SPONGEBOB_HOUSE: 'CustomGamePack' = _common_types.SP68  # 2025-12-04
        SP70_SPONGEBOB_KIDS_ROOM: 'CustomGamePack' = _common_types.SP70  # 2025-12-04
        SP71_GRANGE_MUDROOM: 'CustomGamePack' = _common_types.SP71  # 2025-08-21
        SP81_PRAIRIE_DREAMS: 'CustomGamePack' = _common_types.SP81  # 122 2025-12-11
        SP82_YARD_CHARM: 'CustomGamePack' = _common_types.SP82  # 123 2026-02-26 **tbr**
        SP83: 'CustomGamePack' = _common_types.SP82  # 124 2026-tbd
        # ... SP99 = 140; SP100 = 1256 ... SP124 = 1280

        # Create a Sim Kits
        SP20_THROWBACK_FIT: 'CustomGamePack' = _common_types.SP20
        SP24_FASHION_STREET: 'CustomGamePack' = _common_types.SP24
        SP26_INCHEON_ARRIVALS: 'CustomGamePack' = _common_types.SP26
        SP28_MODERN_MENSWEAR: 'CustomGamePack' = _common_types.SP28
        SP30_CARNAVAL_STREETWEAR: 'CustomGamePack' = _common_types.SP30  # Spanish name (EA)
        SP30_CARNIVAL_STREETWEAR: 'CustomGamePack' = _common_types.SP30  # English name (fix)
        SP32_MOONLIGHT_CHIC: 'CustomGamePack' = _common_types.SP32
        SP34_FIRST_FITS: 'CustomGamePack' = _common_types.SP34
        SP38_SIMTIMATES_COLLECTION: 'CustomGamePack' = _common_types.SP38
        SP42_GRUNGE_REVIVAL: 'CustomGamePack' = _common_types.SP42
        SP44_POOLSIDE_SPLASH: 'CustomGamePack' = _common_types.SP44
        SP48_GOTH_GALORE: 'CustomGamePack' = _common_types.SP48
        SP50_URBAN_HOMAGE: 'CustomGamePack' = _common_types.SP50
        SP56_SWEET_SLUMBER_PARTY: 'CustomGamePack' = _common_types.SP56
        SP62_BUSINESS_CHIC: 'CustomGamePack' = _common_types.SP62
        SP64_SWEET_ALLURE: 'CustomGamePack' = _common_types.SP64
        SP66_GOLDEN_YEARS: 'CustomGamePack' = _common_types.SP66
        SP69_AUTUMN_APPAREL: 'CustomGamePack' = _common_types.SP69
        SP72_ESSENTIAL_GLAM: 'CustomGamePack' = _common_types.SP72
        SP73_MODERN_RETREAT: 'CustomGamePack' = _common_types.SP73  # 2025-11-13
        SP74_GARDEN_TO_TABLE: 'CustomGamePack' = _common_types.SP74  # 2025-11-13
        SP75_WONDERLAND_PLAYROOM: 'CustomGamePack' = _common_types.SP75  # 116 2026-02-26 **tbr**
        SP76_SILVER_SCREEN_STYLE: 'CustomGamePack' = _common_types.SP76  # 117 2026-02-12
        SP77_TEA_TIME_SOLARIUM: 'CustomGamePack' = _common_types.SP77  # 118 2026-02-12
        SP78: 'CustomGamePack' = _common_types.SP78  # 119 2026-tbd
        SP79: 'CustomGamePack' = _common_types.SP79  # 120 2026-tbd
        SP80: 'CustomGamePack' = _common_types.SP80  # 121 2026-tbd

        # Other Kits
        SP22_BUST_THE_DUST: 'CustomGamePack' = _common_types.SP22  # 43 2021-02-03 ***
        SP59_SECRET_SANCTUARY: 'CustomGamePack' = _common_types.SP59  # 100 2025-01-16
        SP60_CASANOVA_CAVE: 'CustomGamePack' = _common_types.SP60  # 101  2025-01-16

        INVALID: 'CustomGamePack' = _common_types.INVALID  # 255

    except:
        pass
