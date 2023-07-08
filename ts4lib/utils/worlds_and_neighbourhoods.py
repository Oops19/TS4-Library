#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
from typing import Tuple

from sims4communitylib.utils.location.common_location_utils import CommonLocationUtils
from ts4lib.utils.singleton import Singleton


class WorldsAndNeighbourhoods(object, metaclass=Singleton):
    _data = {
        0: ('Unknown', 'Unknown'),
        1902162923: ('Willow Creek', 'Foundry Cove'),
        2363457107: ('Willow Creek', 'Courtyard Lane'),
        2280805822: ('Willow Creek', 'Pendula View'),
        2474553381: ('Willow Creek', 'Sage Estates'),
        2740343228: ('Willow Creek', 'Crawdad Quarter'),
        1232026046: ('Willow Creek', 'Magnolia Blossom Park'),
        3424307691: ('Willow Creek', '(Sylvan Glade)'),  # (Secret Lot)
        3942535330: ('Newcrest', 'Bridgeview'),
        3942535331: ('Newcrest', 'Llama Lagoon'),
        3942535328: ('Newcrest', 'Ridgeline Drive'),
        617967630: ('Oasis Springs', 'Bedrock Strait'),
        711065386: ('Oasis Springs', 'Parched Prospect'),
        3632553424: ('Oasis Springs', 'Skyward Palms'),
        1185542770: ('Oasis Springs', 'Acquisition Butte'),
        1111996224: ('Oasis Springs', 'Mirage Canyon'),
        2842140217: ('Oasis Springs', 'Desert Bloom Park'),
        2648122660: ('Oasis Springs', '(Forgotten Grotto)'),  # (Secret Lot)
        1704446400: ('Magnolia Promenade', '[Get to Work]'),  # [DLC with no named neighborhood]
        2760968765: ('Magnolia Promenade', '(Sixam)'),  # (Secret Lot)
        3691563516: ('Windenburg', 'Olde Platz'),
        1267499153: ('Windenburg', 'Lykke Centre'),
        3398743073: ('Windenburg', 'Windslar'),
        1084260742: ('Windenburg', 'The Crumbling Isle'),
        2475261189: ('Windenburg', 'Von Haunt Estate'),
        3982447363: ('Windenburg', 'Ancient Ruins'),
        1469628631: ('Windenburg', 'The Bluffs'),
        4131314756: ('Granite Falls', 'Campground'),
        2609254731: ('Granite Falls', 'Granite Falls Forest'),
        3505758661: ('Granite Falls', '(Hermit’s House)'),  # (Secret Lot)
        1456220773: ('San Myshuno', 'Spice Market'),
        1075237116: ('San Myshuno', 'Arts Quarter'),
        4034911840: ('San Myshuno', 'Fashion District'),
        3428213867: ('San Myshuno', 'Uptown'),
        1788497979: ('San Myshuno', 'Myshuno Meadows'),
        3864949102: ('Brindleton Bay', 'Sable Square'),
        2893613071: ('Brindleton Bay', 'Whiskerman’s Wharf'),
        1906928472: ('Brindleton Bay', 'Cavalier Cove'),
        1685642028: ('Brindleton Bay', 'Deadgrass Isle'),
        3950992577: ('Forgotten Hollow', '[Vampires]'),  # [DLC with no named neighborhood]
        1634851428: ('Selvadorada', 'Puerto Llamante Marketplace'),
        345901884: ('Selvadorada', 'Belomisia Jungle'),
        # -52: ('Selvadorada', 'Jungle District'),
        2018586480: ('StrangerVille', 'StrangerVille Plaza'),
        3934213596: ('StrangerVille', 'Shady Acres'),
        3327507166: ('StrangerVille', 'The Secret Lab'),
        2323227531: ('Del Sol Valley', 'Mirage Park'),
        1420552844: ('Del Sol Valley', 'The Pinnacles'),
        3882972916: ('Del Sol Valley', 'Starlight Boulevard'),
        3834550333: ('Del Sol Valley', 'Plumbob Pictures'),  # Career Lot?
        1549761885: ('Sulani', 'Mua Pel’am'),
        1893347376: ('Sulani', 'Ohan’ali Town'),
        3105469928: ('Sulani', 'Lani St. Taz'),
        1465961617: ('Britechester', 'Foxbury Institute'),
        2371324614: ('Britechester', 'Gibbs Hill'),
        12452862: ('Britechester', 'University of Britechester'),
        100140133: ('Glimmerbrook', '[Realm of Magic]'),  # [DLC with no named neighborhood]
        1192736953: ('Glimmerbrook', '(The Magic Realm)'),  # (Secret Lot)
        2496862430: ('Evergreen Harbor', 'Grims Quarry'),
        1821074231: ('Evergreen Harbor', 'Conifer Station'),
        369359163: ('Evergreen Harbor', 'Port Promise'),
        1491052508: ('Mt. Komorebi', 'Wakaba'),
        3002294565: ('Mt. Komorebi', 'Senbamachi'),
        2458782193: ('Mt. Komorebi', 'Yukimatsu'),
        1573360963: ('Batuu', 'Black Spire Outpost'),
        2574008666: ('Batuu', 'First Order District'),
        3755578420: ('Batuu', 'Resistance Encampment'),
        2650041621: ('Henford-on-Bagley', 'Finchwick'),
        14190941: ('Henford-on-Bagley', 'Old New Henford'),
        3913092862: ('Henford-on-Bagley', 'The Bramblewood'),
        3442073656: ('Tartosa', 'Porto Luminoso'),  # My Wedding Stories
        493539179: ('Tartosa', 'Terra Amorosa'),  # My Wedding Stories
        1812713502: ('Moonwood Mill', '[Werewolves]'),  # [DLC with no named neighborhood]
        1505295608: ('Copperdale', 'Plumbite Cove'),  # HSY
        3013809927: ('Copperdale', 'Prescott Square'),  # HSY
        3741233432: ('Copperdale', 'Rockridge Heights'),  # HSY
        3927353875: ('San Sequoia', 'Anchorpoint Wharf'),  # Growing Together
        2596862512: ('San Sequoia', 'Gilbert Gardens'),  # Growing Together
        3962653297: ('San Sequoia', 'Hopewell Hills'),  # Growing Together
    }

    def __init__(self):
        self.clu = CommonLocationUtils()

    def get_world_and_neighbourhood_name(self, world_id: int = None) -> Tuple[str, str]:
        if world_id is None:
            world_id = self.clu.get_current_world_id()
        world_name, neighbourhood_name = self._data.get(world_id, self._data.get(0))
        return world_name, neighbourhood_name

    def get_world_name(self, world_id: int = None) -> str:
        world_name, _ = self.get_world_and_neighbourhood_name(world_id)
        return world_name

    def get_neighbourhood_name(self, world_id: int = None) -> str:
        _, neighbourhood_name = self.get_world_and_neighbourhood_name(world_id)
        return neighbourhood_name
