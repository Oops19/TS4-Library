#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.common_enums.enum_types.common_enum import CommonEnum


class UnCommonMessageType(CommonEnum):
    INVALID: 'UnCommonMessageType' = 0
    ERROR: 'UnCommonMessageType' = 1
    WARN: 'UnCommonMessageType' = 2
    INFO: 'UnCommonMessageType' = 3
    DEBUG: 'UnCommonMessageType' = 4
    TRACE: 'UnCommonMessageType' = 5
