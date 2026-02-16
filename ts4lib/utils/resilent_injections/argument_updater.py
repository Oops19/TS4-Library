#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


from typing import Tuple, Callable, Any, Dict

r"""
from ts4lib.modinfo import ModInfo

from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'ArgumentsUpdater')
log.enable()
"""


class ArgumentsUpdater:
    r"""
    Patch an element which is either in 'args' or in 'kwargs'.
    The callback to patch will always be called when the element is in 'args' or 'kwargs'.
    The 1st element is the var_name and the 2nd one is the var_value.
    To patch and add a new kwargs element even if it can't be found set 'add_missing_as_kwarg=True'
    If the element can't be found the callback will be called with parameters ('', None).

    Usage:
    class RandomClass:
        # this is the class we want to inject into. I kept it simple.
            def __init__(self, date :'int', names:'List[str]', ...):
                # self=0th argument, date=1st argument, names=2nd argument
                return

    class Sample:
        def __init__(self):
            # Check whether RandomClass.__init__ has a parameter named car_name at position 2 and is of type List[str]
            # If this test fails self.is_valid is set to 'False'
            self.is_valid = InjectionUtility.check_signature(RandomClass, '__init__', {'names': (2, List[str])})
            if self.is_valid:
                self.inject_into_random_class()

        @staticmethod
        def patch_value(var_name: str, var_value: Any):
            # In this example the 1st if check never match as 'add_missing_as_kwarg=False' and 'var_name="names"'
            if var_value is None and var_name is '':
                # The variable var_name has not been found - it will be added as kwargs!
                return ["test", "test-2", ]

            # Here comes more custom sample code
            if var_name == "names":  # in case this method is used to patch multiple variables make sure to patch the right one. Otherwise, skip this check.
                if isinstance(var_value, Set) or isinstance(var_value, Tuple):
                    # Do not underestimate the stupidy of EA! Keep this check and convert to a list
                    var_value = list(var_value)
                if isinstance(var_value, list):  # Keep this check!
                    # Do not underestimate the stupidy of EA! Modify this value only if it is a List.
                    var_value.append("test"")
            return var_value
        return var_value  # should never happen, in such a case we patch nothing

        @staticmethod
        def inject_into_random_class()
            @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), RandomClass, '__init__')
            def _inject_into_random_class(original, self, *args, **kwargs):
                args, kwargs = ArgumentsUpdater.update(args, kwargs, "name", 2, Sample.patch_value, add_missing_as_kwarg=False)
                return original(self, *args, **kwargs)

    """

    @staticmethod
    def is_valid_index(t: Tuple[Any, ...], index: int) -> bool:
        return 0 <= index < len(t)

    @staticmethod
    def _get_element(t: Tuple[Any, ...], index: int) -> Any:
        return t[index]

    @staticmethod
    def _update(t: Tuple[Any, ...], index: int, value: Any) -> Tuple[Any, ...]:
        """Return a new tuple with the n-th element replaced. """
        temp = list(t)
        temp[index] = value
        return tuple(temp)

    @classmethod
    def update( cls, args: Tuple[Any, ...], kwargs: Dict[str, Any], kwarg_key: str, arg_index: int, callback: Callable, add_missing_as_kwarg: bool = False, ) -> Tuple[Tuple[Any, ...], Dict[str, Any]]:
        """
        Update either kwargs[kwarg_key] or args[arg_index] using the callback.
        Preference: kwargs first, fallback to args. If args fail to 'add_missing_as_kwarg' is evaluated.
        :param args: The 'args' parameters to parse.
        :param kwargs: The 'kwargs' parameters to parse.
        :param kwarg_key: The key to modify in kwargs. If not found, arg_index will be used to patch args.
        :param arg_index: The 'index' to access an element within 'args'. Set this to -1 to keep all 'args' values as-is.
        :param callback: A method to modify the found value.
        :param add_missing_as_kwarg: A new 'kwarg_key' will be added in case 'kwargs' doesn't contain it and no 'args[arg_index]' could be found. Set to 'True' to enable this behaviour.
        :return:
        """
        if kwarg_key in kwargs:
            kwargs[kwarg_key] = callback(kwarg_key, kwargs[kwarg_key])
        elif cls.is_valid_index(args, arg_index):
            element = cls._get_element(args, arg_index)
            args = cls._update(args, arg_index, callback(kwarg_key, element))
        elif add_missing_as_kwarg:
            kwargs[kwarg_key] = callback('', None)
        return args, kwargs
