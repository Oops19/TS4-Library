# TS4 Library
A small library of methods I use often. It doesn't replace S4CL which is still used for logging.

### 3D Stuff
Generic Euler, 2D, 3D and 4D vector functions.

#### Animation
The `TS4LibraryPoseInteraction` class to support basic animations and poses.

### BasicExtras
Generate a 'basic_extras' tuning to be inserted into an instanced tuning object.

### CommonEnum
A clone of the Python Enum with support for `@_missing_` to return a default value.
Supports various TS4 enums.

### FileUtils
Search for files in a base folder and get the absolute or relative file name f(base_folder)

### FNV
FNV uses the TS4 hash methods when available and otherwise a Python implementation.

### Outfit Utils
For now just a method to apply an outfit to a sim.
If only the previous outfit_index exists and the chosen one is valid and unused a new outfit will be created.  

### PrettyDict
A small utility to write Dict data formatted human-readable.

### RunCommands
Added the ability to run 'execute' or 'client_cheat' commands.
This functionality will be removed from [RunCheatCommands](https://github.com/Oops19/TS4-RunCheatCommands) and integrated here.

### SimName
Get the classic 'sim_name' as one string (e.g. 'Ann Lee#Smith' or 'Ann#Lee Smith') with '#' as a separator between the first and the last names.

### SimCache
A cache for all loaded sims. See below.

### Simple Notification
Display a simple notification.

### Singleton
A random Singleton class for Python.

### Tuning Helper
A simple class to access the instanced tuning classes.

### TS4Folders
Provides access to the 'The Sims 4' folders.

### UnCommonLog
A logger which works without TS4 running, to test parts of Mods locally and later in-game without changing the code.

### VanillaNames (Location)
Handler for more files to get human-readable names.

### WorldsAndNeighbourhoods
Access the world name (Newcrest) and the neighbourhood (Llama Lagoon) with the English description.



## Details and Examples

### 3D Stuff
Generic functions which are available for all 3D classes:

Operations
* `3d == 3d`  # True/False
* `3d.equals(3d, tolerance=0.1)`  # True/False
* `3d = 3d + 3d`
* `3d = 3d - 3d`
* `3d = 3d.def randomize()`
* `length = 3d.magnitude()`
* `length = 3d.length()`
* `_ = 3d.serialize()`  # E.g. `{'std_euler_angle.StdEulerAngle': (0.0, 0.0, 0.0)}`
* `3d = VectorInterface().deserialize(3d.serialize())`  # The correct object type is returned (StdEulerAngle/StdQuaternion/StdVector)

Output
* `3d` # (0, 0, 0) / (1.571, 3.142, 4.712) - print with 3 digits unless they are '0'
* `3d.vector()`  # [1.5707963267948966, 3.141592653589793, 4.71238898038469]
* `3d.as_list()`  # [1.5707963267948966, 3.141592653589793, 4.71238898038469]
* `3d.as_tuple()`  # (1.5707963267948966, 3.141592653589793, 4.71238898038469)
* `3d.format(digits=5, unit='µm', separator='/', left_str='<', right_str='>', multiplier=0.5)` # <0.78540µm/1.57080µm/2.35619µm>
* `3d.format(..., digits=2, keep_trailing_zero=True)` # (0.00, 0.00, 0.00) instead of (0, 0, 0)
 
#### StdEulerAngle
A basic implementation to store euler angles.

Initialization
* `StdEulerAngle(roll=0, pitch=0, yaw=0)`
* `StdEulerAngle((0,0,0))`  # or [0,0,0]
* `StdEulerAngle(..., convert_deg_to_rad=True)`  # Specify angles in deg. Output will be in deg.

Operations
* `StdQuaternion = StdEulerAngle().quaternion()`
* `StdEulerAngle = StdEulerAngle().cross_prod(StdEulerAngle())`
* `StdEulerAngle = StdEulerAngle() * StdEulerAngle()`

Output
* `StdEulerAngle(1.571, 3.142, 4.712)`  # (1.571, 3.142, 4.712)
* `StdEulerAngle(1.571, 3.142, 4.712).rad()`  # (1.571, 3.142, 4.712)
* `StdEulerAngle(1.571, 3.142, 4.712).deg()`  # (90.0°, 180.0°, 270.0°)
* `StdEulerAngle(90, 180, 270, True)`  # (90°, 180°, 270°)
* `StdEulerAngle(90, 180, 270, True).deg()`  # (90°, 180°, 270°)
* `StdEulerAngle(90, 180, 270, True).rad()`  # (1.571, 3.142, 4.712)

#### StdQuaternion
A simple quaternion (w, x, y, z)` implementation to rotate vectors and quaternions.
The TS4 Quaternion uses a different order (x, y, z, w) of parameters!

Initialization
* Quaternions will not be normalized during initialization
* `StdQuaternion(w=1, x=0, y=0, z=0)`
* `StdQuaternion((1,0,0,0))`  # or [1,0,0,0]
* `StdQuaternion(StdQuaternion())`  # or StdVector3() or StdVector2()

Operations
* Operations usually return a normalized quaternion
* `StdQuaternion = StdQuaternion().normalize()`  # normalized
* `StdEulerAngle = StdQuaternion().add(StdQuaternion())`  # normalized
* `StdEulerAngle = StdQuaternion().sub(StdQuaternion())`  # normalized
* `StdQuaternion = StdQuaternion().divide(StdQuaternion())`  # normalized
* `StdQuaternion = StdQuaternion().multiply(StdQuaternion())`  # normalized
* `StdQuaternion = StdQuaternion().conjugate()`  # NOT normalized
* `StdQuaternion = StdQuaternion() + StdQuaternion()`  # NOT normalized
* `StdQuaternion = StdQuaternion() - StdQuaternion()`  # NOT normalized
* `StdQuaternion = StdQuaternion() * StdQuaternion()`  # NOT normalized
* `StdQuaternion = StdQuaternion() / StdQuaternion()`  # NOT normalized
* `StdEulerAngle = StdQuaternion().euler_angles()`
* `[roll, pitch, yaw] = StdQuaternion().get_euler_angles()`
* `StdVector3 = StdQuaternion().rotate_vector(StdVector3())` 
* `StdVector3 = StdQuaternion().rotate_vector(StdQuaternion())`  # w should be 0
* `sims4.math.Quaternion = StdQuaternion().as_ts4_quaternion()`

#### StdVector3
A very basic `StdVector3(x, y, z)` implementation. Should be compatible with the TS4 Vector3D. 
The axis directions may not match the TS4 standard.

Initialization
* `StdVector3(x=0, y=0, z=0)`
* `StdVector3((0,0,0))`  # or [0,0,0]
* `StdVector3(StdVector3())`  # or StdQuaternion() or StdVector2()

Operations
* `StdVector3 = StdVector3() + StdVector3()`
* `StdVector3 = StdVector3() - StdVector3()`
* `float = StdVector3() * StdVector3()`  # dot / scalar product
* `float = StdVector3().dot(StdVector3())`  # deprecated,  dot / scalar product
* `float = StdVector3().scalar(StdVector3())`  # deprecated,  dot / scalar product
* `float = StdVector3().cross(StdVector3())`  # cross product
* `float = StdVector3().length()`  # The length of the vector
* `sims4.math.Vector3 = StdVector3().as_ts4_vector3()`

#### StdVector2
A very basic `StdVector2(x, y)` implementation. Should be compatible with the TS4 Vector2D. 
The axis directions may not match the TS4 standard.

Initialization
* `StdVector2(axis_1=0, axis_2=0)`
* `StdVector2((0,0))`  # or [0,0]
* `StdVector2(StdVector2())`  # or StdVector3() or StdQuaternion()
* `StdVector2(..., axis_names=('x', 'y'))`  # or ['x', 'y'] - to define the name for the 1st and 2nd axis, e.g. ('x', 'z'). This is important when converting to StdVector3 or StdQuaternion.

Operations
* `StdVector2 = StdVector2() + StdVector2()`
* `StdVector2 = StdVector2() - StdVector2()`
* `float = StdVector2() * StdVector2()`  # dot / scalar product
* `float = StdVector2().dot(StdVector2())`  # deprecated,  dot / scalar product
* `float = StdVector2().scalar(StdVector2())`  # deprecated,  dot / scalar product
* `float = StdVector2().cross(StdVector2())`  # The value for the 3rd axis of a Std3DVector that is perpendicular (⦝) to the two vectors.
* `StdVector3 = StdVector2().cross_3d(StdVector2())`  # A Std3DVector that is perpendicular (⦝) to the two vectors.
* `float = StdVector2().length()`  # The length of the vector
* `sims4.math.Vector2 = StdVector3().as_ts4_vector2()`  # Convert to a TS4 2D vector. x=first axis, y=second axis.

#### StdVector4
A very basic `StdVector4(w, x, y, z)` implementation to store invalid quaternions as used by TS4.

#### Animation
The `TS4LibraryPoseInteraction` class to support basic animations and poses.

### BasicExtras
Generate a 'basic_extras' tuning to be inserted into an instanced tuning object.

### CommonEnum
A clone of the Python Enum with support for `@_missing_` to return a default value.

#### Age(CommonEnum)
* `'BABY' == Age['BABY'].name`
* `1 == Age(1).value`
* `Age['BABY'] == Age(1)`
* `list(Age.__members__.keys()) == ['NONE', 'BABY', 'TODDLER', 'CHILD', 'TEEN', 'YOUNGADULT', 'YOUNG_ADULT', 'ADULT', 'ELDER', 'INFANT', 'TYAE']`
* `[e.value for e in Age] == list(map(lambda c: c.value, Age)) == [0, 1, 2, 4, 8, 16, 32, 64, 128, 120]`
* `Age.__members__.values() == odict_values([<Age.NONE: 0>, <Age.BABY: 1>, ...])`
* * `for i in Foo.__members__.values():`
* * * `print(f"{i.name}: {i.value}")`  # NONE: 0
* `Age.__members__.items() == odict_items([('NONE', <Age.NONE: 0>), ('BABY', <Age.BABY: 1>), ...])`
* * `for k,v in Foo.__members__.items():`
* * * `print(f"{k}: ({v.name} {v.value})")`  # NONE: (NONE 0)

#### Gender(CommonEnum)
see `Age`

### FileUtils
Search for files in a base folder and get the absolute or relative file name f(base_folder)

### FNV
FNV uses the TS4 hash methods when available and otherwise a Python implementation.
It supports all kind of FNV32 and FNV64 calculation with custom prime numbers and strings. It supports UTF-8 and mixed lower/upper case.
The cheat command `o19.ts4l.test_fnv foo` outputs the FNV values to the console and the log file.
```python
from ts4lib.utils.fnv import FNV
text = "𝄞 ♯𝅗𝅥♮𝅘𝅥♭𝅘𝅥𝅮"
s = FNV().get(text, 64, ucs2=True, ascii_2_lower=True, set_high_bit=True)
text = b'text'
s = FNV().get(text, 32)
```
### Outfit Utils
For now just a method to apply an outfit to a sim.
If only the previous outfit_index exists and the chosen one is valid and unused a new outfit will be created.  

### PrettyDict
A small utility to write Dict data formatted human-readable.
It avoids data conversion to JSON. 
```python
from ts4lib.utils.config.pretty_dict import PrettyDict
...
```
### RunCommands
Added the ability to run 'execute' or 'client_cheat' commands.
This functionality will be removed from [RunCheatCommands](https://github.com/Oops19/TS4-RunCheatCommands) and integrated here.

### SimName
Get the classic 'sim_name' as one string (e.g. 'Ann Lee#Smith' or 'Ann#Lee Smith') with '#' as a separator between the first and the last names.

### SimCache
A cache for all loaded sims.

This mod caches sim data for easy access.
Other mods can use the sim list to support searching for sims.
One can enter the full sim name or only parts of it.

Query parameter examples:
* 'Bella#Goth' should find 'Bella Goth', usually only one sim is named like this.
* 'Be#Go' should find 'Bella Goth' and/or 'Ben God', ...
* 'b#g' should find 'Bella Goth' and other sims with the same initials.
* 'la#th' should find 'Bella Goth' and other sims with the last name characters as 'la' and 'th'. It will also match 'Lale Thix'
* 'a#h' should find 'Bella Goth' and other sims with the last name characters as 'a' and 'h'
* 'l#o' should also find 'Bella Goth' as the characters match.


* If there are 1-n exact matches they will be used. 
* * Else if there are 1-n matches with 'starts/initials' they will be used. 
* * Else if there are 1-n matches with 'ends' they will be used. 
* * Else if there are 1-n matches with 'contains' they will be used.


#### Script Commands:
```python
sc = SimCache()  # Singleton, if one instance exists already it will be used.
sim_ids = sc.gender_female  # gender_male
sim_ids = sc.age_baby  # age_infant, age_toddler, age_child, age_teen, age_young_adult, age_adult, age_elder; _age_tyae
sim_ids = sc.species_human  # species_animal, species_cat, species_dog, species_fox, species_horse, species_large_dog, species_pet, species_small_dog 
sim_ids = sc.occult_human  # occult_alien, occult_ghost, occult_mermaid, occult_plant_sim, occult_robot, occult_scarecrow, occult_skeleton, occult_vampire, occult_werewolf, occult_witch
# occult_human contains sim_ids without any other occults.
sim_ids = sc.get_sim_ids_by_occult_types([OccultType.WITCH, 'Robot', ])
sim_ids = sc.get_sim_ids_by_ages([Age.BABY, 'Adult', ])
sim_ids = sc.get_sim_ids_by_ids([1, 2, 3, ])
sim_ids = sc.get_sim_ids_by_genders([Gender.MALE, 'Male', ])
match_sim_ids, equals_sim_ids, starts_sim_ids, ends_sim_ids, contains_sim_ids = sc.get_sim_ids_by_sim_name('b#g')
# join results with `&` and/or `|`
```

#### Cheat Commands
* 'o19.ts4l.sc.search firstname#lastname' - Search for a sim. If the first or last name has a space put in in quotes. Use '#' as a separator between the first and last name. 'Ann Ting#Lee' is not Ann#Ting Lee'!
* 'o19.ts4l.sc.refresh' - Only newly created sims will be detected when loading into a zone. Use this command to detect name and gender changes without re-starting the games. 
* 'o19.ts4l.sc.dump' - Dump all data to log.


### Simple Notification
Display a simple notification with `SimpleUINotification().show('title', 'message')` (blue), optionally as a warning with `..., UiDialogNotification.UiDialogNotificationUrgency.URGENT)` (orange).

### Singleton
A random Singleton class for Python. Usage: `Foo(object, metaclass=Singleton):` instead of `Foo:`.

### Tuning Helper
A simple method `get_tuning_ids(manager, tuning)` to access the instanced tuning classes (no longer in XML form).
The manager is not required and tunings can be the 's' IDs or the 'n' names, wildcards are supported to match multiple tunings.  

### TS4Folders
Provides access to the TS4⁽¹⁾/Game, TS4⁽²⁾/Mods and TS4⁽²⁾/mod_data folder.
* TS4⁽¹⁾ is not TS4⁽²⁾.
* In TS4⁽¹⁾ are 'Game', 'Data', 'Delta' and installed DLCs like 'EP01', 'GP01', 'FP01', 'SP01', ...
* In TS4⁽²⁾ are 'Mods', 'GameVersion.txt', Mods, 'mod_logs', 'mod_data', 'mod_documentation', ...

### UnCommonLog
A logger which works without TS4 running, to test parts of Mods locally and later in-game without changing the code.
```python

from {TODO_MOD_NAME}.modinfo import ModInfo
try:
    from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
    log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
except:
    from ts4lib.utils.un_common_log import UnCommonLog
    log: UnCommonLog = UnCommonLog(f"{ModInfo.get_identity().name}", ModInfo.get_identity().name, custom_file_path=None)
log.enable()
```

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
This mod has been tested with `The Sims 4` 1.108.349, S4CL 3.7, TS4Lib 0.3.24 (2024-07-25).
It is expected to be compatible with many upcoming releases of TS4, S4CL and TS4Lib.

## Dependencies
Download the ZIP file, not the sources.
* [This Mod](../../releases/latest)
* [TS4-Library](https://github.com/Oops19/TS4-Library/releases/latest)
* [S4CL](https://github.com/ColonolNutty/Sims4CommunityLibrary/releases/latest)
* [The Sims 4](https://www.ea.com/games/the-sims/the-sims-4)

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
* © 2024 [Oops19](https://github.com/Oops19)
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
