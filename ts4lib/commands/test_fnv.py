#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#
#


from ts4lib.modinfo import ModInfo
from ts4lib.utils.fnv import FNV

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommandArgument, CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog


log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity().name, ModInfo.get_identity().name)
log.enable()


class TestFnv:
    """Simple code snippet to check the FNV implementation."""

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.fnv.test', 'Verify FNV key generation.',
                          command_arguments=(
                                  CommonConsoleCommandArgument('text', 'string', 'The text to convert.', is_optional=False),
                          )
                          )
    def o19_fnv_test(output: CommonConsoleCommandOutput, text: str):
        try:
            output(f"Testing '{text}'")
            try:
                import sims4.commands
                import sims4
                import sims4.hash_util
                ts4_32 = sims4.hash_util.hash32(text)
            except Exception as e:
                output(f"TS4 could not generate hash32! ({e}")
                ts4_32 = 0
            try:
                import sims4.commands
                import sims4
                import sims4.hash_util
                ts4_64 = sims4.hash_util.hash64(text)
            except Exception as e:
                output(f"TS4 could not generate hash64! ({e}")
                ts4_64 = 0

            fnv = FNV()
            fnv_32 = fnv.get(text, 32, ascii_2_lower=True, ucs2=True, set_high_bit=False)  # !fnv.hash32()
            fnv64 = fnv.get(text, 64, ascii_2_lower=True, ucs2=True, set_high_bit=False)  # !fnv.hash64()
            if (fnv_32 == ts4_32) and (fnv64 == ts4_64):
                output(f"OK - 32: 0x{fnv_32:08X} - 64: 0x{fnv64:016X}")
                log.info(f"0x{fnv_32:08X} = {fnv_32} = fnv32('{text}')")
                log.info(f"0x{fnv64:08X} = {fnv64} = fnv64('{text}')")
            else:
                output(f"ERROR: fnv32 = 0x{fnv_32:08X} ≠ ts4_32 = 0x{fnv_32:08X}")
                output(f"ERROR: fnv64 = 0x{fnv64:016X} ≠ ts4_64 = 0x{ts4_64:016X}")
        except Exception as e:
            output(f"Oops: {e}")
            log.error(f"Oops: {e}", throw=True)
