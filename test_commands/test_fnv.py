#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#


if __name__ == '__main__':
    from ts4lib.utils.fnv import FNV
    fnv = FNV()

    text = 'Hello'
    ts4_ascii_2_lower = True
    ts4_ucs2 = False
    for n in [24, 32, 56, 64]:
        for ts4_set_high_bit in [False, True]:

            value = fnv.get(text, n=n, ascii_2_lower=ts4_ascii_2_lower, ucs2=ts4_ucs2, set_high_bit=ts4_set_high_bit)
            if n <= 32:
                print(f"t={text}, n={n}, h={int(ts4_set_high_bit)}, v=0x{value:08X}")
            else:
                print(f"t={text}, n={n}, h={int(ts4_set_high_bit)}, v=0x{value:016X}")
