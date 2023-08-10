#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#

if __name__ == '__main__':
    from ts4lib.utils.fnv import FNV

    fnv = FNV()
    print(fnv.hash64('Hello'))
