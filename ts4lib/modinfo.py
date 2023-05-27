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
        return '0.0.19'


'''
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
