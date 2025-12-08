#
# © 2024 https://github.com/Oops19
# LICENSE
# I grant you a personal, limited, non-transferable (i.e., not for sharing), revocable and non-exclusive license to use this mod to which you have access for your non-commercial use, subject to your compliance with this Agreement.
# You may not copy, modify or distribute my mod, unless expressly authorized by me or permitted by law.
# You may not reverse engineer or attempt to extract or otherwise use source code or other data from my mod, unless expressly authorized.
# I own and reserve all other rights.
#


from typing import Union, Tuple

from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton

from distributor.shared_messages import IconInfoData
from ui.ui_dialog_notification import UiDialogNotification

from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SimpleUINotification')
log.enable()


class SimpleUINotification(metaclass=Singleton):
    def show(self, title: Union[str, int], message: Union[str, int], title_tokens: Tuple = (), description_tokens: Tuple = (), urgency: int = None, icon: IconInfoData = None, secondary_icon: IconInfoData = None):
        r"""
        Simple method to show a notification.
        Display a title string and a description string: 'show('TITLE', 'Message')' - no i18n / STBL support when using it like this.
        Display a static STBL title and STBL message: 'show(1234, 6789)'
        Display a dynamic STBL tile and STBL message: 'show(2222, 3333, (sim_info, ), ('1000', ))'
        :param title: Static string or STBL number
        :param message: Static string or STBL number
        :param title_tokens: Optional tuple with tokens for the title
        :param description_tokens: Optional tuple with tokens for the message
        :param urgency: Optional parameter to change th urgency to critical (orange box)
        :param icon: Optional primary icon to display. (e.g. IconInfoData(obj_instance=CommonSimUtils.get_sim_instance(sim_info)))
        :param secondary_icon: Optional secondary icon to display.
        :return:
        """
        try:
            log.debug(f"{title}: '{message}' ({urgency})")
        except Exception as e:
            pass
        try:
            if isinstance(title, int) and title <= 0xFFFF_FFFF:
                title_identifier = title
                title_tokens = title_tokens
            else:
                title_identifier = 0xFC089996  # '{0.String}'
                title_tokens = (title,)

            if isinstance(message, int) and message <= 0xFFFF_FFFF:
                description_identifier = message
                description_tokens = description_tokens
            else:
                description_identifier = 0xFC089996  # '{0.String}'
                description_tokens = (message,)

            if urgency is None:
                urgency = UiDialogNotification.UiDialogNotificationUrgency.DEFAULT

            basic_notification = CommonBasicNotification(
                title_identifier,
                description_identifier,
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                urgency=urgency,
            )
            basic_notification.show(icon=icon, secondary_icon=secondary_icon)
        except Exception as e:
            log.warn(f"Error: {e}")
