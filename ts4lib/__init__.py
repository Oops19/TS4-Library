#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2025 https://github.com/Oops19
#


import sys
import os


# On macOS, remove ts4l_ctypes from sys.path to prevent import errors
if sys.platform == "darwin":
    p = os.path.join(os.path.dirname(__file__), "ts4l_ctypes")
    if p in sys.path:
        sys.path.remove(p)
    p = os.path.join(os.path.dirname(__file__), "ts4l_ctypes", "macholib")
    if p in sys.path:
        sys.path.remove(p)
