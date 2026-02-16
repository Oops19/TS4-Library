
from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.service.custom_event import custom_event
from ts4lib.utils.simple_ui_notification import SimpleUINotification
from ts4lib.utils.worlds_and_neighbourhoods import WorldsAndNeighbourhoods


class PopupWorldInfo:

    @staticmethod
    @custom_event(CustomEvent.ZONE_CLEANUP_OBJECTS)
    def show_popup(*args, **kwargs):
        try:
            wan = WorldsAndNeighbourhoods()
            pack, world_name, neighbourhood_name = wan.get_pack_world_and_neighbourhood()
            SimpleUINotification().show(f"{world_name} ({pack})", neighbourhood_name, urgency=1)
        except Exception as e:
            SimpleUINotification().show('Error', f"{e}")
