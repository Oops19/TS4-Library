#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


class frozendict(dict):
    r"""
    Usage:
    try:
        # noinspection PyUnresolvedReferences
        from _sims4_collections import frozendict
    except:
        # Import simple frozendict
        from ts4lib.custom_enums.enum_types.frozendict import frozendict
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hash = None

    def __setitem__(self, key, value):
        raise TypeError("frozendict is immutable")

    def __delitem__(self, key):
        raise TypeError("frozendict is immutable")

    def clear(self):
        raise TypeError("frozendict is immutable")

    def pop(self, *args, **kwargs):
        raise TypeError("frozendict is immutable")

    def popitem(self):
        raise TypeError("frozendict is immutable")

    def setdefault(self, *args, **kwargs):
        raise TypeError("frozendict is immutable")

    def update(self, *args, **kwargs):
        raise TypeError("frozendict is immutable")

    def __hash__(self):
        # Cache the hash for efficiency
        if self._hash is None:
            # Hash based on items (order-independent)
            self._hash = hash(frozenset(self.items()))
        return self._hash
