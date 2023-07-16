# TS4 Library
A small library of methods I use often. It doesn't replace S4CL which is still used for logging.

### BasicExtras
Generate a 'basic_extras' tuning to be inserted into an instanced tuning object.

### CommonEnum
A clone of the Python Enum with support for `@_missing_` to return a default value.

### FileUtils
Search for files in a base folder and get the absolute or relative file name f(base_folder)

### FNV
FNV uses the TS4 hash methods when available and otherwise a Python implementation.
It supports all kind of FNV32 and FNV64 calculation with custom prime numbers and strings. It supports UTF-8 and mixed lower/upper case.
The cheat command `o19.ts4l.test_fnv foo` outputs the FNV values to the console and the log file.

### Outfit Utils
For now just a method to apply an outfit to a sim.
If only the previous outfit_index exists and the chosen one is valid and unused a new outfit will be created.  

### SimName
Get the classic 'sim_name' as one string (e.g. 'Ann Lee#Smith' or 'Ann#Lee Smith') with '#' as a separator between the first and the last names.

### Singleton
A random Singleton class for Python. Usage: `Foo(object, metaclass=Singleton):` instead of `Foo:`.

### Tuning Helper
A simple method `get_tuning_ids(manager, tuning)` to access the instanced tuning classes (no longer in XML form).
The manager is not required and tunings can be the 's' IDs or the 'n' names, wildcards are supported to match multiple tunings.  

### TS4Folders
Provides access to the TS4⁽¹⁾/Game, TS4⁽²⁾/Mods and TS4⁽²⁾/mod_data folder.
* TS4⁽¹⁾ is not TS4⁽²⁾.
* In TS4⁽¹⁾ are 'Game', 'Data', 'Delta' and Installed DLCs like 'EP01', 'GP01', 'FP01', 'SP01', ...
* In TS4⁽²⁾ are 'Mods', 'GameVersion.txt', Mods, 'mod_logs', 'mod_data', 'mod_documentation', ...

### UnCommonLogger
A logger which works without TS4 running, to test parts of Mods locally and later in-game without changing the code.

### VanillaNames (Location)
Handler for more `vanilla_*.py` files to get human-readable strings. To retrieve human-readable, English, descriptions about the active zone use:
* r = VanillaNames.from_enum(VanillaRegions(getattr(services.current_region(), 'guid64', 0))) 
* v = VanillaNames.from_enum(VanillaVenues(getattr(services.get_current_venue(), 'guid64', 0)))

To convert such a string back to an enum use the enum class and the string and call e.g.
* enum = VanillaNames.to_enum(VanillaRegions, 'Career Alien World')
* enum = VanillaNames.to_enum('ts4lib.common_enums.vanilla_regions.VanillaRegions', 'Career Alien World')

The command `o19.ts4l.log_location` makes use of many functions added to this class to retrieve friendly names.

### WorldsAndNeighbourhoods
Access the world name (Newcrest) and the neighbourhood (Llama Lagoon) with the English description.
It's meant to be written to configuration files to help the player to customize worlds and/or neighbourhoods.
To retrieve this information for the active zone use:
* w, n = WorldsAndNeighbourhoods().get_world_and_neighbourhood_name(CommonLocationUtils().get_current_world_id())


# Addendum

## Game compatibility
This mod has been tested with `The Sims 4` 1.98.158 (2023-06), S4CL 2.7 (2023-06), TS4Lib 0.0.24 (2023-06).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [TS4Lib](https://github.com/Oops19/TS4-Library/releases/latest)

If not installed download and install TS4 and these mods.
All are available for free.

## Installation
* Locate the localized `The Sims 4` folder which contains the `Mods` folder.
* Extract the ZIP file into this `The Sims 4` folder.
* It will create the directories/files `Mods/_o19_/$mod_name.ts4script`, `Mods/_o19_/$mod_name.package`, `mod_data/$mod_name/*` and/or `mod_documentation/$mod_name/*`
* `mod_logs/$mod_name.txt` will be created as soon as data is logged.

### Manual Installation
If you don't want to extract the ZIP file into `The Sims 4` folder you might want to read this. 
* The files in `ZIP-File/mod_data` are usually required and should be extracted to `The Sims 4/mod_data`.
* The files in `ZIP-File/mod_documentation` are for you to read it. They are not needed to use this mod.
* The `Mods/_o19_/*.ts4script` files can be stored in a random folder within `Mods` or directly in `Mods`. I highly recommend to store it in `_o19_` so you know who created it.

## Usage Tracking / Privacy
This mod does not send any data to tracking servers. The code is open source, not obfuscated, and can be reviewed.

Some log entries in the log file ('mod_logs' folder) may contain the local username, especially if files are not found (WARN, ERROR).

## External Links
[Sources](https://github.com/Oops19/)
[Support](https://discord.gg/d8X9aQ3jbm)
[Donations](https://www.patreon.com/o19)

## Copyright and License
* © 2023 [Oops19](https://github.com/Oops19)
* License for '.package' files: [Electronic Arts TOS for UGC](https://tos.ea.com/legalapp/WEBTERMS/US/en/PC/)  
* License for other media unless specified differently: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) unless the Electronic Arts TOS for UGC overrides it.
This allows you to use this mod and re-use the code even if you don't own The Sims 4.
Have fun extending this mod and/or integrating it with your mods.

Oops19 / o19 is not endorsed by or affiliated with Electronic Arts or its licensors.
Game content and materials copyright Electronic Arts Inc. and its licensors. 
Trademarks are the property of their respective owners.

### TOS
* Please don't put it behind a paywall.
* Please don't create mods which break with every TS4 update.
* For simple tuning modifications use [Patch-XML](https://github.com/Oops19/TS4-PatchXML) 
* or [LiveXML](https://github.com/Oops19/TS4-LiveXML).
* To check the XML structure of custom tunings use [VanillaLogs](https://github.com/Oops19/TS4-VanillaLogs).
