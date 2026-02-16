from sims4communitylib.services.commands.common_console_command import CommonConsoleCommand
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.sims.common_sim_utils import CommonSimUtils
from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.modinfo import ModInfo
from ts4lib.service.custom_event import custom_event
from ts4lib.utils.interaction.enqueue_interaction import EnqueueInteraction
from ts4lib.utils.simple_ui_notification import SimpleUINotification
from ts4lib.utils.worlds_and_neighbourhoods import WorldsAndNeighbourhoods


class PopupWorldInfo:
    r"""
    @staticmethod
    @custom_event(CustomEvent.ZONE_CLEANUP_OBJECTS)
    def show_popup(*args, **kwargs):
        try:
            wan = WorldsAndNeighbourhoods()
            pack, world_name, neighbourhood_name = wan.get_pack_world_and_neighbourhood()
            SimpleUINotification().show(f"{world_name} ({pack})", neighbourhood_name, urgency=1)
        except Exception as e:
            SimpleUINotification().show('Error', f"{e}")

    """

    @staticmethod
    @CommonConsoleCommand(
        ModInfo.get_identity(), 'o19.burst', "Apply a random mood ...",)
    def o19_cmd_doll_mood_random(output: CommonConsoleCommandOutput):
        try:
            sim = CommonSimUtils.get_active_sim()
            interaction_id = 150575  # vampires_MindPowers_EmotionalBurst_Flirty
            sim_2 = CommonSimUtils.get_sim_instance(249692283129108872)
            EnqueueInteraction().run_interaction(sim, interaction_id, sim_2)
            output(f"OK")
        except Exception as e:
            output(f"Error: {e}")
