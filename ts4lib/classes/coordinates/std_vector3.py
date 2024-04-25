#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
import math
from typing import Union, Any, Tuple, List
from ts4lib.classes.coordinates.vector_interface import VectorInterface


class StdVector3(VectorInterface):
    def __init__(self, x: Union[Union[float, int, Tuple[Union[float, int], Union[float, int], Union[float, int]], List[Union[float, int]]], "StdQuaternion", "StdVector3", "StdVector2"] = 0.0, y: Union[float, int] = 0.0, z: Union[float, int] = 0.0):
        """
        StdVector3(x, y, z) - TS4 may handle axes differently
        @param x: float - x-axis to the right
        @param y: float - y-axis to the top
        @param z: float - z-axis to the viewer

        @param x: Tuple, List will be treated as a xyz vector
        @param x: StdQuaternion which will be converted to a StdVector3.
        @param x: Std3DVector which will be converted to a StdVector3.
        @param x: Std2DVector which will be converted to a StdVector3.
        @param x: The object needs the attributes 'x', 'y' and 'z' or they are set to 0.
        """
        if isinstance(x, float) or isinstance(x, int):
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        elif (isinstance(x, Tuple) or isinstance(x, List)) and len(x) == 3:
            x, y, z = x
            self.x = float(x)
            self.y = float(y)
            self.z = float(z)
        else:
            for i in ['x', 'y', 'z']:
                setattr(self, i, 0.0 if getattr(x, i, None) is None else getattr(x, i))  # don't copy None
        super().__init__([self.x, self.y, self.z])

    @staticmethod
    def _v(vector) -> "StdVector3":
        if isinstance(vector, StdVector3):
            return vector
        else:
            from ts4lib.classes.coordinates.std_vector2 import StdVector2
            from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
            if isinstance(vector, StdQuaternion) or isinstance(vector, StdVector2):
                return StdVector3(vector)
            else:
                return StdVector3()

    def __add__(self, vector: "StdVector3") -> "StdVector3":
        return StdVector3(*super().__add__(self._v(vector)))

    def __sub__(self, vector: "StdVector3") -> "StdVector3":
        return StdVector3(*super().__sub__(self._v(vector)))

    def __mul__(self, vector: "StdVector3") -> float:
        """
        :param vector: Std3DVector (or 2D or Q), otherwise Std3DVector(0, 0, 0) will be used
        :return: The dot / scalar product
        """
        _vector = self._v(vector)
        return self.x * _vector.x + self.y * _vector.y + self.z * _vector.z

    def dot(self, vector: "StdVector3") -> float:
        """ Deprecated, use 'self * vector' """
        return self * vector

    def scalar(self, vector: "StdVector3") -> float:
        """ Deprecated, use 'self * vector' """
        return self * vector

    def cross(self, vector: "StdVector3") -> "StdVector3":
        """
        Calculate 'self × vector'
        :param vector: Std3DVector (or 2D or Q), otherwise Std3DVector(0, 0, 0) will be used
        :return: A vector that is perpendicular (⦝) to the two vectors.
        """
        _vector = self._v(vector)
        return StdVector3(
            self.y * _vector.z - self.z * _vector.y,
            self.z * _vector.x - self.x * _vector.z,
            self.x * _vector.y - self.y * _vector.x,
        )

    def length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def as_ts4_vector3(self):
        try:
            # noinspection PyUnresolvedReferences
            from sims4.math import Vector3, Quaternion, Transform, Location
            return Vector3(self.x, self.y, self.z)
        except:
            pass
        return None

    def randomize(self) -> "StdVector3":
        return StdVector3(*super().randomize())
