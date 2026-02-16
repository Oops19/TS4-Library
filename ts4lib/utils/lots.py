r"""
placeholder class
Lots are stored in LotDescriptionResource: 01942E2C
  e.g:
  "LotId": "0x8465000D",
  "BuildingNameKey": "0xECAD83E7", - often 0 !
  stbl(  "BuildingNameKey": "0xECAD83E7",) = b'Taka Soi 15',
    "DisplayName": "Taka Soi 15",

if BuildingNameKey == 0:
    HouseholdDescriptionResource: 729F6C4F
      "LotNameHash": "0xF13BE6C5", --> stbl() ==> b'Laurel Library',  # 0000000000036500
      LotDescription -> 00000000000364FB === "LotId": "0xE6960073",


#
    HouseholdDescriptionResource: 729F6C4F
  "LotNameHash": "0xB9222671", b'Spring Steppes'
  "LotDescriptionHash": "0x7909DDD2", b'As one of the two ..."
    "LotDescription": "0x00000000000361AD",  ==>   "LotId": "0xE6B10052",
  "HouseholdNameHash": "0xA50DCFFA", b'Elderberry',
  "HouseholdDescriptionHash": "0x4A6AB51B", 0x4A6AB51B: b"Ekram and Eleanore have ..."


These are the default lot names - it may be impossible to retrieve manually set lot names.

class Lots(object, metaclass=Singleton):
    # small list f(LotDescriptionResource)
    _data: Dict[int, str] = {
        0: 'Unknown',
        0x59CC0003: "Jasmine Suites Apartments",  # EP03 City Living
        0x00007530:  "ArtsLight_lot03",
        0x66140004: "Hakim House Apartments",
        0x3AC10003: : "Medina Studios Apartments",
        0x67150007: "ArtsLight_lot03",
        0x96440004: "Spire Apartments",
        0x965F0005: "Landgraab Apartments",
        0x960D0003: "Alto Apartments",
        0x0BAB0004:  "Culpepper Apartments",
        0x57420003: "21 Chic Street Apartments",
        0x57490004: "ZenView Apartments",

        0x17FD0334:  "Pinecrest Apartments",  # EP09 Eco Lifestyle
        0x62710031:  "Stonestreet Apartments",

        0xD0D7000C: "Sungai Point",  # EP15 For Rent
        0x8465000D: "Taka Soi 15",

        0xF60A0089: "Bright Cliff Apartments",  # EP21
        0x8CC70091: "Lakeview Apartments",

    }
"""