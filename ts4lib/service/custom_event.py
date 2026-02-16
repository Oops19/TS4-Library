#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from ts4lib.custom_enums.custom_event import CustomEvent
from ts4lib.service.custom_injections import CustomInjections


def custom_event(evt: CustomEvent):
    def wrapper(func):
        CustomInjections().register_event(evt, func)
        return func
    return wrapper
