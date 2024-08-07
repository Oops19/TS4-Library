#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton
from ui.ui_dialog_notification import UiDialogNotification
from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.services.commands.common_console_command_output import CommonConsoleCommandOutput
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SimpleUINotification')
log.enable()


class SimpleUINotification(metaclass=Singleton):
    def show(self, title, message, urgency: "UiDialogNotification.UiDialogNotificationUrgency" = None, output: "CommonConsoleCommandOutput" = None):
        try:
            log.debug(f"{title}: '{message}' ({urgency})")
        except Exception as e:
            pass
        try:

            if urgency is None:
                urgency = UiDialogNotification.UiDialogNotificationUrgency.DEFAULT
            basic_notification = CommonBasicNotification(
                0xFC089996,  # '{0.String}'
                0xFC089996,  # '{0.String}'
                title_tokens=(title,),
                description_tokens=(message,),
                urgency=urgency
            )
            basic_notification.show()
        except Exception as e:
            pass
