#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.custom_enums.enum_types.custom_enum import CustomEnum


class UnCommonMessageType(CustomEnum):
    INVALID: 'UnCommonMessageType' = 0
    ERROR: 'UnCommonMessageType' = 1
    WARN: 'UnCommonMessageType' = 2
    INFO: 'UnCommonMessageType' = 3
    DEBUG: 'UnCommonMessageType' = 4
    TRACE: 'UnCommonMessageType' = 5
