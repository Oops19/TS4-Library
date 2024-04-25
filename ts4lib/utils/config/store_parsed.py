#
# LICENSE
# https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.utils.singleton import Singleton


class StoreParsed(object, metaclass=Singleton):
    """
    Create a custom Reader to add data to this store.
    After reading the files a property will be added to this class.
    It can be accessed with getattr(StoreParsed(), f"{base_namespace}_{file_name}")
    This store contains processed / converted data.
    """
    pass
