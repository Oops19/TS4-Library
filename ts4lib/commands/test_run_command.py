#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.modinfo import ModInfo
from ts4lib.utils.commands.run_commands import RunCommands

from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand, CommonConsoleCommandArgument
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput


class TestRunCommand:

    @staticmethod
    @CommonConsoleCommand(ModInfo.get_identity(), 'o19.ts4l.runcmd', "Run a single cheat command. E.g. e o19.rcc testing_cheats true. To add more than one parameter use \"\" (not '') around them.",
                          command_arguments=(
                                  CommonConsoleCommandArgument('type', 'string', "'e' or 'c' for 'execute()' or 'client_cheat()'", is_optional=False),
                                  CommonConsoleCommandArgument('command', 'string', 'The command to be run, optionally use \"\" to add 1-n parameters.', is_optional=False),
                                  CommonConsoleCommandArgument('parameter', 'string', 'The command parameter(s), if any.', is_optional=True, default_value=''),
                          )
                          )
    def o19_run_cheat_commands_test(output: CommonConsoleCommandOutput, command_type: str, command: str, parameter: str = ''):
        """
        To test whether execute() or cheat_command() should be used. If there is no output except of 'OK' this may be really tricky.
        Add the command later to commands.ini.
        """
        try:
            rc = RunCommands()
            if parameter:
                command = f"{command} {parameter}"
            output(f"Running '{command_type}' ({command})")
            if command_type == 'e':
                rv = rc.execute_command(command)
                if not rv:
                    output(f"Exception: {rc.last_exception}")
            elif command_type == 'c':
                rv = rc.client_cheat_command(command)
                if not rv:
                    output(f"Exception: {rc.last_exception}")
            else:
                output(f"Unknown type '{command_type}'. Only 'e' (execute_command) and 'c' (client_cheat_command) are supported.")
                return
            output('OK')
        except Exception as e:
            output(f"Oops: {e}")
