#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Tuple, Set, List, Dict

from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from ts4lib.custom_enums.custom_game_pack import CustomGamePack
from ts4lib.utils.singleton import Singleton


class WorldsAndNeighbourhoods(object, metaclass=Singleton):
    _data: Dict[int, Tuple[str, str, str]] = {
        0: (CustomGamePack.NONE, 'Unknown', 'Unknown'),
        1902162923: (CustomGamePack.BASE_GAME, 'Willow Creek', 'Foundry Cove'),
        2363457107: (CustomGamePack.BASE_GAME, 'Willow Creek', 'Courtyard Lane'),
        2280805822: (CustomGamePack.BASE_GAME, 'Willow Creek', 'Pendula View'),
        2474553381: (CustomGamePack.BASE_GAME, 'Willow Creek', 'Sage Estates'),
        2740343228: (CustomGamePack.BASE_GAME, 'Willow Creek', 'Crawdad Quarter'),
        1232026046: (CustomGamePack.BASE_GAME, 'Willow Creek', 'Magnolia Blossom Park'),
        3424307691: (CustomGamePack.BASE_GAME, 'Willow Creek', '(Sylvan Glade)'),  # (Secret Lot)
        3942535330: (CustomGamePack.BASE_GAME, 'Newcrest', 'Bridgeview'),
        3942535331: (CustomGamePack.BASE_GAME, 'Newcrest', 'Llama Lagoon'),
        3942535328: (CustomGamePack.BASE_GAME, 'Newcrest', 'Ridgeline Drive'),
        617967630: (CustomGamePack.BASE_GAME, 'Oasis Springs', 'Bedrock Strait'),
        711065386: (CustomGamePack.BASE_GAME, 'Oasis Springs', 'Parched Prospect'),
        3632553424: (CustomGamePack.BASE_GAME, 'Oasis Springs', 'Skyward Palms'),
        1185542770: (CustomGamePack.BASE_GAME, 'Oasis Springs', 'Acquisition Butte'),
        1111996224: (CustomGamePack.BASE_GAME, 'Oasis Springs', 'Mirage Canyon'),
        2842140217: (CustomGamePack.BASE_GAME, 'Oasis Springs', 'Desert Bloom Park'),
        2648122660: (CustomGamePack.BASE_GAME, 'Oasis Springs', '(Forgotten Grotto)'),  # (Secret Lot)

        4131314756: (CustomGamePack.GP01_OUTDOOR_RETREAT, 'Granite Falls', 'Campground'),
        2609254731: (CustomGamePack.GP01_OUTDOOR_RETREAT, 'Granite Falls', 'Granite Falls Forest'),
        3505758661: (CustomGamePack.GP01_OUTDOOR_RETREAT, 'Granite Falls', '(Hermit’s House)'),  # (Secret Lot)
        3950992577: (CustomGamePack.GP04_VAMPIRES, 'Forgotten Hollow', '[Vampires]'),  # GP04_VampireWorld_01 [DLC with no named neighborhood]
        1634851428: (CustomGamePack.GP06_JUNGLE_ADVENTURES, 'Selvadorada', 'Puerto Llamante Marketplace'),  # GP06_MarketPlace_01
        345901884: (CustomGamePack.GP06_JUNGLE_ADVENTURES, 'Selvadorada', 'Belomisia Jungle'),  # GP06_Jungle_01
        # -52: (CustomGamePack.GP06_JUNGLE_ADVENTURES, 'Selvadorada', '[Discover Jungle Secret]'),  # ''
        2018586480: (CustomGamePack.GP07_STRANGERVILLE, 'StrangerVille', 'StrangerVille Plaza'),
        3934213596: (CustomGamePack.GP07_STRANGERVILLE, 'StrangerVille', 'Shady Acres'),
        3327507166: (CustomGamePack.GP07_STRANGERVILLE, 'StrangerVille', 'The Secret Lab'),
        100140133: (CustomGamePack.GP08_REALM_OF_MAGIC, 'Glimmerbrook', '[Realm of Magic]'),  # [DLC with no named neighborhood]
        1192736953: (CustomGamePack.GP08_REALM_OF_MAGIC, 'Glimmerbrook', '(The Magic Realm)'),  # (Secret Lot)
        1573360963: (CustomGamePack.GP09_STAR_WARS_JOURNEY_TO_BATUU, 'Batuu', 'Black Spire Outpost'),
        2574008666: (CustomGamePack.GP09_STAR_WARS_JOURNEY_TO_BATUU, 'Batuu', 'First Order District'),
        3755578420: (CustomGamePack.GP09_STAR_WARS_JOURNEY_TO_BATUU, 'Batuu', 'Resistance Encampment'),
        3442073656: (CustomGamePack.GP11_MY_WEDDING_STORIES, 'Tartosa', 'Porto Luminoso'),  # My Wedding Stories
        493539179: (CustomGamePack.GP11_MY_WEDDING_STORIES, 'Tartosa', 'Terra Amorosa'),  # My Wedding Stories
        1812713502: (CustomGamePack.GP12_WEREWOLVES, 'Moonwood Mill', '[Werewolves]'),  # [DLC with no named neighborhood]

        1704446400: (CustomGamePack.EP01_GET_TO_WORK, 'Magnolia Promenade', '[Get to Work]'),  # [DLC with no named neighborhood]
        2760968765: (CustomGamePack.EP01_GET_TO_WORK, 'Magnolia Promenade', '(Sixam)'),  # (Secret Lot)
        3691563516: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'Olde Platz'),
        1267499153: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'Lykke Centre'),
        3398743073: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'Windslar'),
        1084260742: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'The Crumbling Isle'),
        2475261189: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'Von Haunt Estate'),
        3982447363: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'Ancient Ruins'),
        1469628631: (CustomGamePack.EP02_GET_TOGETHER, 'Windenburg', 'The Bluffs'),
        1456220773: (CustomGamePack.EP03_CITY_LIVING, 'San Myshuno', 'Spice Market'),
        1075237116: (CustomGamePack.EP03_CITY_LIVING, 'San Myshuno', 'Arts Quarter'),
        4034911840: (CustomGamePack.EP03_CITY_LIVING, 'San Myshuno', 'Fashion District'),
        3428213867: (CustomGamePack.EP03_CITY_LIVING, 'San Myshuno', 'Uptown'),
        1788497979: (CustomGamePack.EP03_CITY_LIVING, 'San Myshuno', 'Myshuno Meadows'),
        3864949102: (CustomGamePack.EP04_CATS_AND_DOGS, 'Brindleton Bay', 'Sable Square'),
        2893613071: (CustomGamePack.EP04_CATS_AND_DOGS, 'Brindleton Bay', 'Whiskerman’s Wharf'),
        1906928472: (CustomGamePack.EP04_CATS_AND_DOGS, 'Brindleton Bay', 'Cavalier Cove'),
        1685642028: (CustomGamePack.EP04_CATS_AND_DOGS, 'Brindleton Bay', 'Deadgrass Isle'),
        2323227531: (CustomGamePack.EP06_GET_FAMOUS, 'Del Sol Valley', 'Mirage Park'),
        1420552844: (CustomGamePack.EP06_GET_FAMOUS, 'Del Sol Valley', 'The Pinnacles'),
        3882972916: (CustomGamePack.EP06_GET_FAMOUS, 'Del Sol Valley', 'Starlight Boulevard'),
        3834550333: (CustomGamePack.EP06_GET_FAMOUS, 'Del Sol Valley', 'Plumbob Pictures'),  # Career Lot?
        1549761885: (CustomGamePack.EP07_ISLAND_LIVING, 'Sulani', 'Mua Pel’am'),
        1893347376: (CustomGamePack.EP07_ISLAND_LIVING, 'Sulani', 'Ohan’ali Town'),
        3105469928: (CustomGamePack.EP08_DISCOVER_UNIVERSITY, 'Sulani', 'Lani St. Taz'),
        1465961617: (CustomGamePack.EP08_DISCOVER_UNIVERSITY, 'Britechester', 'Foxbury Institute'),
        2371324614: (CustomGamePack.EP08_DISCOVER_UNIVERSITY, 'Britechester', 'Gibbs Hill'),
        12452862: (CustomGamePack.EP08_DISCOVER_UNIVERSITY, 'Britechester', 'University of Britechester'),
        2496862430: (CustomGamePack.EP09_ECO_LIFESTYLE, 'Evergreen Harbor', 'Grims Quarry'),
        1821074231: (CustomGamePack.EP09_ECO_LIFESTYLE, 'Evergreen Harbor', 'Conifer Station'),
        369359163: (CustomGamePack.EP09_ECO_LIFESTYLE, 'Evergreen Harbor', 'Port Promise'),
        1491052508: (CustomGamePack.EP10_SNOWY_ESCAPE, 'Mt. Komorebi', 'Wakaba'),
        3002294565: (CustomGamePack.EP10_SNOWY_ESCAPE, 'Mt. Komorebi', 'Senbamachi'),
        2458782193: (CustomGamePack.EP10_SNOWY_ESCAPE, 'Mt. Komorebi', 'Yukimatsu'),
        2650041621: (CustomGamePack.EP11_COTTAGE_LIVING, 'Henford-on-Bagley', 'Finchwick'),
        14190941: (CustomGamePack.EP11_COTTAGE_LIVING, 'Henford-on-Bagley', 'Old New Henford'),
        3913092862: (CustomGamePack.EP11_COTTAGE_LIVING, 'Henford-on-Bagley', 'The Bramblewood'),
        1505295608: (CustomGamePack.EP12_HIGH_SCHOOL_YEARS, 'Copperdale', 'Plumbite Cove'),  # HSY
        3013809927: (CustomGamePack.EP12_HIGH_SCHOOL_YEARS, 'Copperdale', 'Prescott Square'),  # HSY
        3741233432: (CustomGamePack.EP12_HIGH_SCHOOL_YEARS, 'Copperdale', 'Rockridge Heights'),  # HSY
        3927353875: (CustomGamePack.EP13_GROWING_TOGETHER, 'San Sequoia', 'Anchorpoint Wharf'),  # Growing Together
        2596862512: (CustomGamePack.EP13_GROWING_TOGETHER, 'San Sequoia', 'Gilbert Gardens'),  # Growing Together
        3962653297: (CustomGamePack.EP13_GROWING_TOGETHER, 'San Sequoia', 'Hopewell Hills'),  # Growing Together
        525851134: (CustomGamePack.EP14_HORSE_RANCH, 'Chestnut Ridge', 'Galloping Gulch'),  # Horse Ranch, 3 lots 1
        2808195162: (CustomGamePack.EP14_HORSE_RANCH, 'Chestnut Ridge', 'New Appaloosa'),  # Horse Ranch, 5 lots
        657881596: (CustomGamePack.EP14_HORSE_RANCH, 'Chestnut Ridge', "Rider’s Glen"),  # Horse Ranch, 5 lots
        4017562985: (CustomGamePack.EP15_FOR_RENT, 'Tomarang', 'Morensong'),  # For Rent, 4 lots
        934162359: (CustomGamePack.EP15_FOR_RENT, 'Tomarang', 'Koh Sahpa'),  # For Rent, 5 lots
        2950084182: (CustomGamePack.EP16_LOVESTRUCK, 'Ciudad Enamorada', 'Vista Hermosa'),  # LovesTruck, 5 lots
        271937272: (CustomGamePack.EP16_LOVESTRUCK, 'Ciudad Enamorada', 'Nuevo Corazón'),  # LovesTruck, 4 lots
        1794983438: (CustomGamePack.EP16_LOVESTRUCK, 'Ciudad Enamorada', 'Plaza Mariposa'),  # LovesTruck, 4 lots
        # EP17 'World Map' ->  WorldId: 0x18D53A6A 0x83A3DEAF 0x160307BB
        # 'World Description' -> WorldName + Name + fnv32(Name)
        # Mourningvale + EP17_Afterlife_01 = 160307BB
        # HeadlessQuarters + EP17_Grim_01 = F3240686
        # Whispering Glen + EP17_Countryside_01 = 18D53A6A
        # Crow's Crossing + EP17_Village_01 = 83A3DEAF
        0x83A3DEAF: (CustomGamePack.EP17_LIFE_AND_DEATH, 'Ravenwood', "Crow's Crossing"),  # Life & Death
        0x18D53A6A: (CustomGamePack.EP17_LIFE_AND_DEATH, 'Ravenwood', "Whispering Glen"),  # Life & Death
        0x160307BB: (CustomGamePack.EP17_LIFE_AND_DEATH, 'Ravenwood', "Mourningvale"),  # Life & Death
        0xF3240686:  (CustomGamePack.EP17_LIFE_AND_DEATH, 'Ravenwood', "HeadlessQuarters"),  # Life & Death (hidden)
        # EP18 'World Map' ->  WorldId: 0x96190C2F 0xED9D6B84
        # 'World Description' -> WorldName + Name + fnv(Name)
        # Gammelvik + EP18_OldTown_01 = 96190C2F
        0x96190C2F: (CustomGamePack.EP18_BUSINESS_AND_HOBBIES, 'Nordhaven', 'Gammelvik'),  # Businesses & Hobbies
        0xED9D6B84: (CustomGamePack.EP18_BUSINESS_AND_HOBBIES, 'Nordhaven', 'Iverstad'),  # Businesses & Hobbies
        # EP19 'World Map' -> WorldId 0x72A3C3B6 0xC76C7956 0x98F181DE
        # 'World Description' -> WorldName + Name + fnv(Name)
        # Coast of Adhmor + EP19_Coastal_01 = 72A3C3B6
        # Sprucederry Grove + EP19_Grove_01 = 98F181DE
        0x72A3C3B6: (CustomGamePack.EP19_ENCHANTED_BY_NATURE, 'Innisgreen', 'Coast of Adhmor'),  # Enchanted by Nature
        0x98F181DE: (CustomGamePack.EP19_ENCHANTED_BY_NATURE, 'Innisgreen', 'Sprucederry Grove'),  # Enchanted by Nature
        0xC76C7956: (CustomGamePack.EP19_ENCHANTED_BY_NATURE, 'Innisgreen', 'Everdew'),  # Enchanted by Nature
        # EP20 'World Map' -> WorldId 0x6B94000A 0x44B02139 0xA5D4ECB3
        # 'World Description' -> WorldName + Name + fnv32(Name)
        # Wanderwood Wilds + EP20_Wilderness_01 = A5D4ECB3
        # Crystal Valley + EP20_GoldenRetreat_01 = 44B02139
        0xA5D4ECB3: (CustomGamePack.EP20_ADVENTURE_AWAITS, 'Gibbi Point', 'Wanderwood Wilds'),  # Adventure Awaits  # 0x6E0490E2
        0x44B02139: (CustomGamePack.EP20_ADVENTURE_AWAITS, 'Gibbi Point', 'Jellyfish Junction'),  # Adventure Awaits
        0x6B94000A: (CustomGamePack.EP20_ADVENTURE_AWAITS, 'Gibbi Point', 'Crystal Valley'),  # Adventure Awaits
        # EP21 'World Description': WorldName + Name --> fnv32(Name); WorldName=stbl(WorldNameKey)
        # 'Region Description': stbl(RegionNameKey) -> Ondarion
        0x76747004: (CustomGamePack.EP21_ROYALTY_AND_LEGACY, 'Ondarion', 'Verdemar'),  # EP21_Coast_01 76747004
        0xA0C42899: (CustomGamePack.EP21_ROYALTY_AND_LEGACY, 'Ondarion', 'Bellacorde'),  # EP21_Lake_01 A0C42899
        0x129AABE4: (CustomGamePack.EP21_ROYALTY_AND_LEGACY, 'Ondarion', 'Dambele'),  # EP21_Arid_01 129AABE4
    }

    def __init__(self):
        self.clu = CommonLocationUtils()

    def get_pack_world_and_neighbourhood(self, world_id: int = None) -> Tuple[str, str, str]:
        if world_id is None:
            world_id = self.clu.get_current_world_id()
        pack, world_name, neighbourhood_name = self._data.get(world_id, self._data.get(0))
        return pack, world_name, neighbourhood_name

    def get_world_and_neighbourhood_name(self, world_id: int = None) -> Tuple[str, str]:
        if world_id is None:
            world_id = self.clu.get_current_world_id()
        pack, world_name, neighbourhood_name = self._data.get(world_id, self._data.get(0))
        return world_name, neighbourhood_name

    def get_world_name(self, world_id: int = None) -> str:
        world_name, _ = self.get_world_and_neighbourhood_name(world_id)
        return world_name

    def get_neighbourhood_name(self, world_id: int = None) -> str:
        _, neighbourhood_name = self.get_world_and_neighbourhood_name(world_id)
        return neighbourhood_name

    def get_world_ids(self, world_names: List[str]) -> Set:
        """
        Return all neighbourhood IDs for the supplied list or world_names. A world contains 1-n neighbourhoods.
        """
        rv = set()
        for world_name in world_names:
            if f"{world_name}".isdecimal():
                rv.add(int(world_name))
                continue
            for neighbourhood_id, world_neighbourhood in self._data.items():
                pack, world, neighbourhood = world_neighbourhood
                if world_name == world:
                    rv.add(neighbourhood_id)
                    # don't break, world_name is not unique.
        return rv

    def get_neighbourhood_ids(self, neighbourhood_names: List[str]) -> Set:
        """
        Return all neighbourhood IDs for the supplied list or neighbourhood_names.
        """
        rv = set()
        for neighbourhood_name in neighbourhood_names:
            if f"{neighbourhood_name}".isdecimal():
                rv.add(int(neighbourhood_name))
                continue
            for neighbourhood_id, world_neighbourhood in self._data.items():
                pack, world, neighbourhood = world_neighbourhood
                if neighbourhood_name == neighbourhood:
                    rv.add(neighbourhood_id)
                    break  # neighbourhood_name is unique
        return rv

