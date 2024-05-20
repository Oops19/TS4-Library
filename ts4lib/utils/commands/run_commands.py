#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from time import sleep


import services
import sims4
import sims4.commands
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry
from ts4lib.modinfo import ModInfo
from ts4lib.utils.commands.command_type import CommandType

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), ModInfo.get_identity().name)
log.enable()


class RunCommands:

    def __init__(self):
        self.last_exception = None  # Stores the last exception if one did occur.
        self.client_id = None  # Stores the client_id

    @property
    def _client_id(self) -> int:
        """
        Run this code one time for each new 'RunCommands' instance.
        @return: A client_id.
        """
        if self.client_id is None:
            try:
                self.client_id = services.client_manager().get_first_client().id
            except Exception as e:
                log.warn(f"Error {e} getting client_id.")
                self.client_id = 1
        return self.client_id

    def run_command(self, command: str) -> bool:
        """
        Run either an 'execute' or 'client_cheat' command.
        :param: command - The command to run.
        :return: True if success, otherwise False.
        """
        l_command = command.split(' ', 1)[0]
        if l_command in CommandType.execute:
            return self.execute_command(command)
        elif l_command in CommandType.client_cheat:
            return self.client_cheat_command(command)
        else:
            log.debug(f"run_command (execute): '{command}' ...")
            rv = self.execute_command(command)
            if rv:
                return True
            log.debug(f"run_command (client_cheat): '{command}' ...")
            return self.client_cheat_command(command)

    def execute_command(self, command: str) -> bool:
        """
        Run an 'execute' command.
        :param: command - The command to run.
        :return: True if success, otherwise False.
        """
        try:
            log.debug(f"execute_command: '{command}' ...")
            sims4.commands.execute(command, self._client_id)
            sleep(0.01)
            return True
        except Exception as e:
            log.warn(f"Error '{e}' executing '{command}'")
            self.last_exception = e
            return False

    def client_cheat_command(self, command: str) -> bool:
        """
        Run an 'client_cheat' command.
        :param: command - The command to run.
        :return: True if success, otherwise False.
        """
        try:
            log.debug(f"client_cheat_command: '{command}' ...")
            sims4.commands.client_cheat(command, self._client_id)
            sleep(0.01)
            return True
        except Exception as e:
            log.warn(f"Error '{e}' client-cheating '{command}'")
            self.last_exception = e
            return False
