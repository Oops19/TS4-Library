#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.modinfo import ModInfo
from ts4lib.utils.config.store_parsed import StoreParsed
from ts4lib.utils.config.store_raw import StoreRaw
from ts4lib.utils.objects.lot_objects import LotObjects

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()


class StoreCheats:

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.ts4l.dump_lot_objects', '...', )
    def o19_read_cfg_cheat_init_bbb(output: CommonConsoleCommandOutput):
        try:
            s = StoreRaw()
            for i in dir(s):
                if i.startswith('__') and i.endswith('__'):
                    continue
                log.debug(f"Raw {i}: {getattr(s, i)}")
            s = StoreParsed()
            for i in dir(s):
                if i.startswith('__') and i.endswith('__'):
                    continue
                log.debug(f"Parsed {i}: {getattr(s, i)}")

            output(f"OK")
        except Exception as e:
            log.error(f"{e}")

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.ts4l.dump_objects', '...',)
    def cheat_o19_ts4l_dump_objects(output: CommonConsoleCommandOutput):
        lo = LotObjects()
        log.debug(f"OBJ: {lo.get_objects()}")
        log.debug(f"BLOCKS {lo.get_block_ids()}")
        output(f"OK")
