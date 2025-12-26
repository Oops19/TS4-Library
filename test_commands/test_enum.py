#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#


if __name__ == '__main__':
    from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum

    class Foo(CustomEnum):
        A = 1
        B = 2
        C = 3
        D = 1
        MISSING_VALUE = 0xFFFF  # 2 ** 16 - 1

        @classmethod
        def _missing_(cls, value):
            """
            Return a default or a random enum value.
            @param value: Can either be the value `Enum(value)` (usually int; str or float) or the key `Enum.KEY ==> KEY` (usually str).
            """
            return cls.MISSING_VALUE

    print(f"Keys `Foo.__members__.keys()` = {Foo.__members__.keys()}")
    # ['A', 'B', 'C', 'D']

    print(f"Values `Foo.__members__.values()` = {Foo.__members__.values()}")
    # [odict_values([<Foo.A: 1>, <Foo.B: 2>, <Foo.C: 3>, <Foo.A: 1>])

    print(f"Values `[e.value for e in Foo]` = {[e.value for e in Foo]}")
    # [1, 2, 3]

    print(f"Values `list(map(lambda c: c.value, Foo))` = {list(map(lambda c: c.value, Foo))}")
    # [1, 2, 3]

    print(f"Items `Foo.__members__.items()` = {Foo.__members__.items()}")
    # odict_items([('A', <Foo.A: 1>), ('B', <Foo.B: 2>), ('C', <Foo.C: 3>), ('D', <Foo.A: 1>)])

    print(f"for k, v in Foo.__members__.items():")
    print(f"\tk: v     with v.name: v.value")
    for k, v in Foo.__members__.items():
        print(f"\t{k}: {v} with      {v.name}: {v.value:}")

    enum_string = 'B'
    _enum_str = Foo[enum_string]
    if (_enum_str == Foo.B) and (_enum_str == Foo(2)):
        print(f"Foo['{enum_string}'] == Foo.B == Foo(2)")
    else:
        print(f"Error! Foo['{enum_string}'] ≠ Foo.B ≠ Foo(2)")

    enum_int = 2
    _enum_int = Foo(enum_int)
    if (_enum_str == Foo.B) and (_enum_str == Foo(2)):
        print(f"Foo({enum_int}) == Foo.B == Foo(2)")
    else:
        print(f"Error! Foo({enum_int}) ≠ Foo.B ≠ Foo(2)")

    if (Foo['A'] == Foo['D']) and (Foo['D'] == Foo(1)):
        print(f"Foo['A'] == Foo['D'] == Foo(1)")
    else:
        print(f"Error! Foo['A'] ≠ Foo['D'] ≠ Foo(1)")

