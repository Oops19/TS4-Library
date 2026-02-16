#
# License: https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2026 https://github.com/Oops19
#


import re
import inspect
from typing import Tuple, Dict, Type, Union

from ts4lib.modinfo import ModInfo
from ts4lib.utils.resilent_injections.late_popup_warning import LatePopupWarning

from sims4communitylib.mod_support.mod_identity import CommonModIdentity
from sims4communitylib.utils.common_log_registry import CommonLogRegistry, CommonLog

r"""
log: CommonLog = CommonLogRegistry.get().register_log(ModInfo.get_identity(), 'InjectionUtility')
log.enable()
"""


class InjectionUtility:

    @staticmethod
    def check_signature(
        mod_identity: CommonModIdentity,
        cls,
        method_name: str,
        expected_signature: Dict[str, Tuple[int, Union[Type, str, None]]],
    ) -> bool:
        """
        Check whether a method exists on a class and whether its parameters
        match expected names, positions, and optionally types.

        :param cls: The class to inspect.
        :param method_name: The method name to check.
        :param expected_signature: Dict of {param_name: (expected_index, expected_type)}.
                                   Use -1 as index to skip position check.
                                   Use expected_type=None as type to skip type check (for many methods without type definitions)
                                   Use expected_type='Foo()' for a string test if a type check is not possible.
        :param mod_identity: The calling mod usually "ModInfo.get_identity()"

        :return: True if all names exist and checks pass, False otherwise.
        """

        def is_equal(_expected_type, _actual_annotation):
            # Handle bare types
            if _expected_type == _actual_annotation:
                return True
            # Handle typing generics
            _actual_annotation_str = f"^.*{_actual_annotation}$".replace("[", r"\[.*").replace(']', r'\]')
            _expected_type_str = f"{_expected_type}"
            if re.match(_actual_annotation_str, _expected_type_str):
                return True
            _log.debug(f"expected_type = '{_expected_type_str}'; actual_annotation = '{_actual_annotation_str}'")
            return False

        if mod_identity is None:
            mod_identity = ModInfo.get_identity()
        _log: CommonLog = CommonLogRegistry.get().register_log(mod_identity, 'InjectionUtility')
        _log.enable()

        if not hasattr(cls, method_name):
            m = f"Method {cls.__name__}.{method_name} not found."
            _log.error(m, throw=False)
            LatePopupWarning().add_message(mod_identity.name, m)
            return False

        method = getattr(cls, method_name)
        sig = inspect.signature(method)
        params = list(sig.parameters.values())
        names = [p.name for p in params]

        rv = True
        for name, (expected_index, expected_type) in expected_signature.items():
            if name not in names:
                m = f"Parameter '{name}' not found in {cls.__name__}.{method_name}."
                _log.error(m, throw=False)
                LatePopupWarning().add_message(mod_identity.name, m)
                rv = False
                continue

            actual_index = names.index(name)
            if expected_index != -1 and actual_index != expected_index:
                m = f"Parameter '{name}' in {cls.__name__}.{method_name} is at index '{actual_index}', expected '{expected_index}'."
                _log.error(m, throw=False)
                LatePopupWarning().add_message(mod_identity.name, m)
                rv = False

            actual_annotation = sig.parameters[name].annotation
            if expected_type is None:
                if actual_annotation is not inspect._empty:
                    m = f"Parameter '{name}' is '{actual_annotation}'. Add this to improve your code."
                    _log.info(m)
            if expected_type is not None:
                actual_annotation = sig.parameters[name].annotation
                if actual_annotation is inspect._empty:
                    m = f"Parameter '{name}' has no type annotation."
                    _log.error(m, throw=False)
                    LatePopupWarning().add_message(mod_identity.name, m)
                elif not is_equal(expected_type, actual_annotation, ):
                    m = f"Parameter '{name}' type mismatch: expected '{expected_type}', got '{actual_annotation}'."
                    _log.error(m, throw=False)
                    LatePopupWarning().add_message(mod_identity.name, m)
                    rv = False

        if rv:
            m = f"Method '{cls.__name__}.{method_name}' matches expected signature '{expected_signature}'."
            _log.info(m)
        _log.disable()
        return rv
