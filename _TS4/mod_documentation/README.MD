# TS4 Library
A small library of methods I use often. It doesn't replace S4CL which is still used for logging.

### CommonEnum
A clone of the Python Enum with support for `@_missing_` to return a default value.

### FileUtils
Search for files in a base folder and get the absolute or relative file name f(base_folder)

### TS4Folders
Provides access to the TS4¹/Game, TS4²/Mods and TS4²/mod_data folder.
* TS4¹ is not TS4².
* In TS4²: Installed DLC and game files.
* In TS4²: lastException.txt, GameVersion.txt, Mods, mod_logs, mod_data, ...

### FNV
FNV uses the TS4 hash methods when available and otherwise a Python implementation.
It supports all kind of FNV32 and FNV64 calculation with custom prime numbers and strings. It supports UTF-8 and mixed lower/upper case.

### Singleton
A random Singleton class for Python. Usage: `Foo(object, metaclass=Singleton):` instead of `Foo:`.

### UnCommonLogger
A logger which works without TS4 running, to test parts of Mods locally and later in-game without changing the code.
