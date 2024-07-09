import re
from typing import Tuple, Set, List, Union

from ts4lib.common_enums.body_type import BodyType


class ExcludeFlags:
    @staticmethod
    def print_s4s():
        """
        Print BB code to be copied to the forum.
        @return:
        """
        for k, v in BodyType.__members__.items():
            value = v.value
            if value == 0:
                print(f'[font size="4"]ExcludeFlags: Parts List and Enum/Binary Values[/font]')
                print(f"[spoiler=Spoiler][table][tbody]")
                print(f"[tr][td]Part to Exclude[/td][td]Enum Value[/td][td]Value[/td][td]Binary Value[/td][/tr]")
            elif value == 64:
                print(f"[/tbody][/table][/spoiler]")
                print(f'[font size="4"]ExcludeFlags2: Parts List and Enum/Binary Values[/font]')
                print(f"[spoiler=Spoiler][table][tbody]")
                print(f"[tr][td]Part to Exclude[/td][td]Enum Value[/td][td]Value[/td][td]Binary Value[/td][/tr]")
            if value >= 64:
                value -= 64

            pow = ''
            for n in f"{value}":
                if n in ['1', ]:
                    d = 136
                elif n in ['2', '3', ]:
                    d = 128
                else:
                    d = 8256
                pow = f"{pow}{chr(d + ord(n))}"

            byte_value = f"{2 ** value:064b}"
            byte_value = " ".join(re.findall('(.{4})', byte_value))
            byte_value = re.sub(r'^(0{4} )*', r'', byte_value)
            print(f"[tr][td style='border:1px solid #000;'][div align='left']{k}[/div][/td][td style='border:1px solid #000;'][div align='center']{v.value}[/div][/td][td style='border:1px solid #000;'][div align='center']2{pow}[/div][/td][td style='border:1px solid #000;'][div align='right']{byte_value}[/div][/td][/tr]")
        print(f"[/tbody][/table][/spoiler]")

    @staticmethod
    def get_flags(exclude_items: Union[List, Set, Tuple]) -> Tuple[str, str]:
        """
        @param exclude_items: Items to be hidden by TS4 while this cas part is applied.
        For a 'hat' cas part don't include 'HAT' unless you know what you are doing.
        @return: Strings for exclude_flags_1 and exclude_flags_2
        """
        exclude_flags_1 = 0
        exclude_flags_2 = 0
        for value in exclude_items:
            if isinstance(value, str):
                value = BodyType[value].value
            elif isinstance(value, BodyType):
                value = value.value
            elif not isinstance(value, int):
                print(f"Ignoring {value} !")
            if value < 64:
                exclude_flags_1 += 2 ** value
            else:
                exclude_flags_2 += 2 ** value
        return f"{exclude_flags_1:016X}", f"{exclude_flags_2:016X}"

ef = ExcludeFlags()
# ef.print_s4s()
# e1, e2 = ef.get_flags(["HAIR", "HEAD", "TEETH", "EARRINGS", "GLASSES", "NECKLACE", "LIP_RING_LEFT", "LIP_RING_RIGHT", "NOSE_RING_LEFT", "NOSE_RING_RIGHT", "BROW_RING_LEFT", "BROW_RING_RIGHT", "FACIAL_HAIR", "LIPS_TICK", "EYE_SHADOW", "EYE_LINER", "BLUSH", "FACEPAINT", "EYEBROWS", "EYECOLOR", "MASCARA", "SKINDETAIL_CREASE_FOREHEAD", "SKINDETAIL_FRECKLES", "SKINDETAIL_DIMPLE_LEFT", "SKINDETAIL_DIMPLE_RIGHT", "SKINDETAIL_MOLE_LIP_LEFT", "SKINDETAIL_MOLE_LIP_RIGHT", "EARS", ])
e1, e2 = ef.get_flags(["HAIR", "HEAD", "TEETH", "EARRINGS", "GLASSES", "NECKLACE", "LIP_RING_LEFT", "LIP_RING_RIGHT", "NOSE_RING_LEFT", "NOSE_RING_RIGHT", "BROW_RING_LEFT", "BROW_RING_RIGHT", "FACIAL_HAIR", "EYEBROWS", "EARS", ])
print(f"exclude_flags_1 = {e1}")
print(f"exclude_flags_2 = {e2}")

e1 = 0x200004101FC0FD1E  # Esmeralda_yuBody_EP08HumanoidBotBlueRedBlueRedLauren_BlueRed
print(f"Excluded parts for {e1}:")
for k, v in BodyType.__members__.items():
    if v.value & e1:
        print(f"- {k}")
    else:
        print(f"+ {k}")
