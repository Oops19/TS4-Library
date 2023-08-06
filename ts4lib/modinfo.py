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
        return '0.1.2'


'''
v0.1.2
    Added RunCommands().run('money 100')
v0.1.1
    Added StdEulerAngle, StdQuaternion, StdVector
v0.1.0
v0.0.31
    Added LocationIDs() as a temporary class until S4CL offers more _id() functions.
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
    Joined together some code snippets which will 'never' be added to S4CL
'''
