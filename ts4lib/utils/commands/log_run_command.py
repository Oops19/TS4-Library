#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


from sims4.commands import CommandType, Command
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.modinfo import ModInfo

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


@Command('o19.debug.run', command_type=CommandType.Live, )
def cmd_o19_debug_run(*args, _connection=None):
    log.debug(f"Called: o19.debug.run {args}")
