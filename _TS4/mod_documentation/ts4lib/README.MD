# TS4 Library
A small library of methods I use often. It doesn't replace S4CL which is still used for logging.

## Dependencies
Requires S4CL v2.6

### BasicExtras
Generate a 'basic_extras' tuning to be inserted into an instanced tuning object.

### CommonEnum
A clone of the Python Enum with support for `@_missing_` to return a default value.

### FileUtils
Search for files in a base folder and get the absolute or relative file name f(base_folder)

### Tuning Helper
A simple method `get_tuning_ids(manager, tuning)` to access the instanced tuning classes (no longer in XML form).
The manager is not required and tunings can be the 's' IDs or the 'n' names, wildcards are supported to match multiple tunings.  

### TS4Folders
Provides access to the TS4⁽¹⁾/Game, TS4⁽²⁾/Mods and TS4⁽²⁾/mod_data folder.
* TS4⁽¹⁾ is not TS4⁽²⁾.
* In TS4⁽¹⁾: 'Game', 'Data', 'Delta' and Installed DLCs like 'EP01', 'GP01', 'FP01', 'SP01', ...
* In TS4⁽²⁾: 'Mods', 'GameVersion.txt', Mods, 'mod_logs', 'mod_data', 'mod_documentation', ...

### FNV
FNV uses the TS4 hash methods when available and otherwise a Python implementation.
It supports all kind of FNV32 and FNV64 calculation with custom prime numbers and strings. It supports UTF-8 and mixed lower/upper case.

### Singleton
A random Singleton class for Python. Usage: `Foo(object, metaclass=Singleton):` instead of `Foo:`.

### UnCommonLogger
A logger which works without TS4 running, to test parts of Mods locally and later in-game without changing the code.

## Copyright and License
© 2023 https://github.com/Oops19
https://creativecommons.org/licenses/by/4.0/ unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it within your mod.

This mod is not endorsed by or affiliated with Electronic Arts, or its licensors.
Trademarks are the property of their respective owners.
Game content and materials copyright Electronic Arts Inc. and its licensors.
All Rights Reserved.

* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use Patch-XML https://github.com/Oops19/TS4-PatchXML or LiveXML https://github.com/Oops19/TS4-LiveXML.


