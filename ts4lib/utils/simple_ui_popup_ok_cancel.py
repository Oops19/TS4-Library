#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


from typing import Union, Tuple, Any, Callable

from sims4communitylib.dialogs.ok_cancel_dialog import CommonOkCancelDialog
from sims4communitylib.utils.common_function_utils import CommonFunctionUtils
from ts4lib.modinfo import ModInfo
from ts4lib.utils.singleton import Singleton

from distributor.shared_messages import IconInfoData
from ui.ui_dialog_notification import UiDialogNotification

from sims4communitylib.notifications.common_basic_notification import CommonBasicNotification
from sims4communitylib.utils.common_log_registry import CommonLog, CommonLogRegistry

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'SimplePopupOkCancel')
log.enable()


class SimpleUiPopupOkCancel(metaclass=Singleton):
    def show(self, title: Union[str, int], message: Union[str, int], title_tokens: Tuple = (), message_tokens: Tuple = (), on_completed: Callable = CommonFunctionUtils.noop, ) -> bool:
        r"""
        Simple method to show a popup with OK and Cancel.
        Display a title string and a message string: 'show('TITLE', 'Message')' - no i18n / STBL support when using it like this.
        Display a static STBL title and STBL message: 'show(1234, 6789)'
        Display a dynamic STBL tile and STBL message: 'show(2222, 3333, (sim_info, ), ('1000', ))'
        :param title: Static string or STBL number
        :param message: Static string or STBL number
        :param title_tokens: Optional tuple with tokens for the title
        :param message_tokens: Optional tuple with tokens for the message

        :return:
        """

        def _on_ok_selected(_: Any):
            on_completed(True)

        def _on_cancel_selected(_: Any):
            on_completed(False)

        try:
            if isinstance(title, int) and title <= 0xFFFF_FFFF:
                title_identifier = title
                title_tokens = title_tokens
            else:
                title_identifier = 0xFC089996  # '{0.String}'
                title_tokens = (title,)

            if isinstance(message, int) and message <= 0xFFFF_FFFF:
                description_identifier = message
                description_tokens = message_tokens
            else:
                description_identifier = 0xFC089996  # '{0.String}'
                description_tokens = (message,)

            confirmation = CommonOkCancelDialog(
                title_identifier,
                description_identifier,
                title_tokens=title_tokens,
                description_tokens=description_tokens,
                mod_identity=ModInfo.get_identity()
            )
            confirmation.show(on_ok_selected=_on_ok_selected, on_cancel_selected=_on_cancel_selected)
            return True
        except Exception as e:
            log.warn(f"Error: {e}")