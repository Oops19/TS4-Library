#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Dict, Union

from ts4lib.utils.singleton import Singleton

# noinspection PyBroadException
try:
    import sims4.commands
    import sims4
    import sims4.hash_util
    use_sims4_hash_utils = True
except:
    use_sims4_hash_utils = False


class FNV(metaclass=Singleton):
    """
    Simple class to generate Fowler-Noll-Vo (FNV) values.
    The Sims 4 (TS4) uses FNV a lot and this class will calculate it even without running TS4.
    It supports UCS-2/UTF-16 and UTF-8, conversion to lower case and clearing or setting the high bit.
    Only FNV24, FNV32, FNV56 and FNV64 are supported.

    It can be initialed exactly one time and should be used with FNV().command
    """
    _fnv_primes: Dict[int, int] = {}
    _fnv_hashes: Dict[int, int] = {}

    def __init__(self, fnv_prime_32: int = 16777619, fnv_prime_64: int = 1099511628211, fnv_string: str = 'chongo <Landon Curt Noll> /\\../\\'):
        """
        :param fnv_prime_32: default: 0x01000193 = 16777619
        :param fnv_prime_64: default: 0x00000100000001B3 = 1099511628211
        :param fnv_string: default: 'chongo <Landon Curt Noll> /\\../\\' (with two escaped backslashes)
        """
        self._fnv_primes.update({32: fnv_prime_32, 64: fnv_prime_64})
        fnv_bytes = fnv_string.encode(encoding='utf-8')  # The default ASCII string stays will be still ASCII
        fnv_hash = 0
        for m, prime in self._fnv_primes.items():
            max_size = 2 ** m
            self._fnv_hashes.update({m: self._fnv_UTF8(fnv_bytes, fnv_hash, prime, max_size)})

    # noinspection PyPep8Naming
    @staticmethod
    def _fnv_UTF8(bytez, hash_value, prime, max_size):
        for b in bytez:
            hash_value = (hash_value * prime) % max_size
            hash_value = hash_value ^ b
        return hash_value

    # noinspection PyPep8Naming
    @staticmethod
    def _fnv_UTF16(words, hash_value, prime, max_size):
        for i in range(0, len(words), 2):
            w = words[i] << 8 | words[i+1]
            hash_value = (hash_value * prime) % max_size
            hash_value = hash_value ^ w
        return hash_value

    def hash24(self, text: str, high_bit: bool = None) -> int:
        """
        Calculate and return the FNV32 hash. If available `sims4.hash_util.hash32(text)` is used, otherwise `@get(text, 32)`
        :param text: The string to get the FNV value for.
        :param high_bit: Set the high_bit to 0 (False), to 1 (True), or don't touch it (default None)
        :return: fnv value
        """
        return self._hash_ts4(text, 24, high_bit)

    def hash32(self, text: str, high_bit: bool = None) -> int:
        """
        Calculate and return the FNV32 hash. If available `sims4.hash_util.hash32(text)` is used, otherwise `@get(text, 32)`
        :param text: The string to get the FNV value for.
        :param high_bit: Set the high_bit to 0 (False), to 1 (True), or don't touch it (default None)
        :return: fnv value
        """
        return self._hash_ts4(text, 32, high_bit)

    def hash56(self, text: str) -> int:
        """
        Calculate and return the FNV56 hash for an English STBL (0x00xx_xxx_xxxx_xxxx)
        :param text: The string to get the FNV value for.
        :return: fnv value
        """
        return self._hash_ts4(text, 56, None)

    def hash64(self, text: str, high_bit: bool = None) -> int:
        """
        Calculate and return the FNV64 hash. If available `sims4.hash_util.hash64(text)` is used, otherwise `@get(text, 64)`
        :param text: The string to get the FNV value for.
        :param high_bit: Set the high_bit to 0 (False), to 1 (True), or don't touch it (default None)
        :return: fnv value
        """
        return self._hash_ts4(text, 64, high_bit)

    def _hash_ts4(self, text: str, n: int, high_bit: bool = None) -> int:
        if use_sims4_hash_utils and n in {32, 64}:
            if n == 32:
                hash_value = sims4.hash_util.hash32(text)
            else:
                hash_value = sims4.hash_util.hash64(text)
            if high_bit is False:
                high_value = ((1 << (n - 1)) - 1)  # 0x7FF_FFFF_FFFF_FFFFF | 0x07FF_FFFF
                hash_value = hash_value & high_value
        else:
            hash_value = self.get(text, n, ascii_2_lower=True, ucs2=True)

        if high_bit:
            high_bit_value = 1 << (n - 1)
            hash_value = hash_value | high_bit_value  # 0x8000_0000_0000_0000 | 0x8000_0000
        elif high_bit is False:
            high_bit_value = ((1 << (n - 1)) - 1)  # 0x7FF_FFFF_FFFF_FFFFF | 0x07FF_FFFF
            hash_value = hash_value & high_bit_value

        return hash_value

    def get(self, text: Union[str, bytes], n: int, ascii_2_lower: bool = False, ucs2: bool = False):
        """
        Use @hash32() and @hash64() when writing code to be executed from within TS4.
        The defaults are for normal FNV operations and are not suitable for TS4.
        For TS4 set ucs2=True and ascii_2_lower=True and often also high_bit=True.
        :param text: The string to get the FNV value for. 'bytes' will be converted to a hash without the options 'ascii_2_lower' and/or 'ucs2'.
        :param n: The exponent for the size of the FNV value (2^n) - 24, 32 and 56, 64 are supported (56 is used for i18n in TS4).
        :param ascii_2_lower: ASCII characters in strings may be converted to lower case (not for text: bytes).
        :param ucs2: Strings are converted to UCS-2 (=True) words or UTF8 (=False) bytes to calculate the hash (not for text: bytes).
        :return: The fnv value or 0
        """
        hash_value = 0
        if (n == 24) or (n == 32):
            m = 32
        elif (n == 56) or (n == 64):
            m = 64
        else:
            return hash_value

        max_size = 2 ** m
        prime = self._fnv_primes.get(m)
        hash_value = self._fnv_hashes.get(m)

        if ascii_2_lower:
            text = text.lower()

        if ucs2:
            if isinstance(text, str):
                # € as UCS-2: 0x20AC
                _words = text.encode(encoding='utf-16be')
            else:
                _words = text
            hash_value = self._fnv_UTF16(_words, hash_value, prime, max_size)
        else:
            if isinstance(text, str):
                # € as UTF-8: 0xE2 0x82 0xAC
                _bytes = text.encode(encoding='utf-8')
            else:
                _bytes = text
            hash_value = self._fnv_UTF8(_bytes, hash_value, prime, max_size)

        if n != m:
            hash_value = (hash_value >> n) ^ (hash_value & (1 << n) - 1)

        return hash_value
