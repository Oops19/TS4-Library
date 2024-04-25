#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
import math
from typing import Union, Any, Tuple, List
from ts4lib.classes.coordinates.vector_interface import VectorInterface


class StdVector4(VectorInterface):
    def __init__(self, w: Union[Union[float, int, Tuple[Union[float, int], Union[float, int], Union[float, int], Union[float, int]], List[Union[float, int]]], "StdQuaternion", "StdVector3", "StdVector2"] = 0.0, x: Union[float, int] = 0.0, y: Union[float, int] = 0.0, z: Union[float, int] = 0.0):
        """
        StdVector4(w, x, y, z) - A dummy class to handle 4D vectors which are used by TS4 in a similar ways as quaternions. Mostly as (0, 0, 0, 0) for random reasons.
        @param w: float - x-axis to the right
        @param x: float - x-axis to the right
        @param y: float - y-axis to the top
        @param z: float - z-axis to the viewer

        @param w: Tuple, List will be treated as a xyz vector
        @param w: StdQuaternion which will be converted to a StdVector4.
        @param w: Std3DVector which will be converted to a StdVector4.
        @param w: Std2DVector which will be converted to a StdVector4.
        @param w: The object needs the attributes 'x', 'y' and 'z' or they are set to 0.
        """
        if isinstance(w, float) or isinstance(w, int):
            self.w = float(w)
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        elif (isinstance(w, Tuple) or isinstance(w, List)) and len(w) == 4:
            w, x, y, z = x
            self.w = float(w)
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        else:
            for i in ['w', 'x', 'y', 'z']:
                setattr(self, i, getattr(w, i, 0.0))
        super().__init__([self.w, self.x, self.y, self.z])

    def randomize(self) -> "StdVector4":
        return StdVector4(*super().randomize())
