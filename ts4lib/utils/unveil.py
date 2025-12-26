#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


import random
import re


class Unveil:
    def illuminate(self):
        while True:
            key = random.randint(1, 31)
            prefix = chr(key + 2**5)
            encoded = ''.join(chr(ord(c) ^ key) for c in self)
            if re.match(r'^[^\x00-\x19\x7f]*$', encoded):
                return f"{prefix}{encoded}"
            else:
                """ decode """
    self = lambda self: ''.join(map(lambda c: chr(ord(c) ^ (ord(self[0]) - 32)), self[1:]))
