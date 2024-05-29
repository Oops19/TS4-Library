#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from sims4communitylib.mod_support.common_mod_info import CommonModInfo


class ModInfo(CommonModInfo):
    _FILE_PATH: str = str(__file__)

    @property
    def _name(self) -> str:
        return 'TS4Lib'

    @property
    def _author(self) -> str:
        return 'o19'

    @property
    def _base_namespace(self) -> str:
        return 'ts4lib'

    @property
    def _file_path(self) -> str:
        return ModInfo._FILE_PATH

    @property
    def _version(self) -> str:
        return '0.3.20'


r'''
v0.3.20
    Tested with TS4 v1.107
v.0.3.19
    Add ET (from PatchXML) to format XML
    Fixed ET to avoid line breaks after comments
v.0.3.18
    Add option to exclude files while searching.
    Return files as sorted list instead of set
v0.3.17
    Added 10 new body parts
    Added exclude_flags/exclude_flags.py for offline usage.
v0.3.16
    Logging improvements
v0.3.15
    Fixed import referring to other mod
v0.3.14
    Fix vector rotation - don't normalize q
v0.3.13
    Fix StdEulerAngle, 
v0.3.12
    Refactor fixes
v0.3.11
    Refactor fixes
v0.3.10
    Added StdVector4() to have a store for invalid quaternions which are used by TS4.
v0.3.9
    Moved various CommonEnum classes to 'common_enums' and renamed them.
v0.3.8
    Support initialization of angels, quaternions and vectors with Tuple, List.
v0.3.7
    Added enums: Age, Gender
v0.3.6
    SimpleUINotification().show('title', 'message', UiDialogNotification.UiDialogNotificationUrgency.DEFAULT)
v0.3.5
    find_files(include_sub_directories=True) new option to include (default) / exclude sub directories
v0.3.4
    Added ctypes
v0.3.3
    Added more vector and euler methods
v0.3.2
    Fix to normalize invalid (0000) quaternions, return 1000 in such cases
v0.3.1
    Added more euler related methods
v0.3.0
    Warning: All mods which are using 'ts4lib.classes.math' will no longer work!
    
    Renamed 'ts4lib.classes.math' to 'ts4lib.classes.coordinates'
    Renamed 'std_vector' to 'std_3d_vector'
    Added 'std_2d_vector'
    Added some math functions (+, -, *, cross()) to the vector classes
    Added vector conversions (Quaternion <-> 3DVector <-> 2dVector)
v0.2.3
    TuningHelper / BasicExtras:
    * Added get_tunings() to retun the tunings
    * Added modify_test_globals() to simplify the modification of test_globals
    * Not everything within test_globals is yet supported!
v0.2.2
    TuningHelper / BasicExtras:
    * Allow to remove do_commands
v0.2.1
    TuningHelper / BasicExtras:
    * Add disable_gender_check() support to TuningHelper
v0.2.0
    Removed support to run `debug.eval()` or `debug.exec()` from scripts.
v0.1.10
    Fixed broken list / missing comma
v0.1.9
    Minor adjustments
v0.1.8
    Minor adjustments
v0.1.7
    Updated README for new TS4 version
    added `o19.ts4l.log_location` cheat command
v0.1.6
    Added VanillaObjects. `VanillaObjects.__members__.keys()` is a list with all names to search for objects like 'BAR'
v0.1.5
    More code for VanillaNames
v0.1.4
    Added ConfigIO() to read and write Dict data.
v0.1.3
    Added PrettyDict().write(file_name, data)
v0.1.2
    Added RunCommands().run('money 100')
v0.1.1
    Added StdEulerAngle, StdQuaternion, StdVector
v0.1.0
v0.0.31
    Added LocationIDs() as a temporary class until S4.CL offers more _id() functions.
    This class will not be documented. It will be removed in the near future.
v0.0.30
    Extended VanillaNames to retrieve even more human-readable location strings.
    VanillaNames.get () ==> VanillaNames.from_enum() # '<FOO_BAR: 1>' => 'Foo Bar'
    + VanillaNames.to_enum() # Enum, 'Foo Bar' ==> '<FOO_BAR: 1>'
v0.0.29
    Added SimName
v0.0.28
    Renamed FNV test command and added to README
v0.0.27
    Updated documentations
v0.0.26
    Added VanillaNames.from_enum() to get a (more or less) human-readable name of an enum.
    Added Enums: VanillaVenues and VanillaRegions
v0.0.25
    Added WorldsAndNeighbourhoods
    Fix import in test_enum.py
v0.0.24
    Fix fnv cheat command
v0.0.22
    Fixed Typo
    Code cleanup
v0.0.21
    Added OutfitUtilities, generate missing outfit
v0.0.20
    Added BodyPart(CommonEnum) (last element BodyType.STRETCHMARKS_BACK = 100) 
v0.0.19
    Update README and compile.sh
v0.0.18
    Update README and compile.sh
v0.0.17
    Added BasicExtras (from OID)
v0.0.16
    Added TuningHelper (from Live XML)
v0.0.15
    Relocate README.md
v0.0.14
    Cleanup
v0.0.13
    Moved Singleton to utils/
v0.0.12
    Fixed TS4Folders/Singleton
v0.0.11
    Replaced globals and Class with self
    This should fix up issues with Singleton
v0.0.10
    Added Singleton
v0.0.9
    Moved class vars to self
v0.0.8
    Joined together some code snippets which will 'never' be added to S4.CL
'''
