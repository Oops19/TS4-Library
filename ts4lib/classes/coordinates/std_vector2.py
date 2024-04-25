#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#
import math
from typing import Any, Union, Tuple, List

from ts4lib.classes.coordinates.vector_interface import VectorInterface


class StdVector2(VectorInterface):
    def __init__(self, axis_1: Union[Union[float, int, Tuple[Union[float, int], Union[float, int]], List[Union[float, int]]], "StdQuaternion", "StdVector3", "StdVector2"] = 0.0, axis_2: Union[float, int] = 0.0, axis_names: Tuple[str, str] = ('x', 'y')):
        """
        StdVector2(x, y)
        @param axis_1: float - x-axis to the right @axis_names
        @param axis_2: float - y-axis to the top @axis_names

        @param axis_1: Tuple, List will be treated as a xy vector
        @param axis_1: StdQuaternion which will be converted to a StdVector2.
        @param axis_1: Std3DVector which will be converted to a StdVector2.
        @param axis_1: Std2DVector which will be converted to a StdVector2.
        @param axis_1: The object needs the attributes 'x' and 'y' or they are set to 0.
        @param axis_names: To define other axis names or order to read from an import 2D, 3D or Q: x y and z are supported as e.g. '(x, z)'
        The 3rd unused axis will be None
        """
        self.x = None
        self.y = None
        self.z = None
        self.axis_names = axis_names

        name_1, name_2 = self.axis_names
        self.axis_3 = None
        if isinstance(axis_1, float) or isinstance(axis_1, int):
            self.axis_1 = float(axis_1)
            self.axis_2 = float(axis_2)
            setattr(self, name_1, axis_1)
            setattr(self, name_2, axis_2)
        elif (isinstance(axis_1, Tuple) or isinstance(axis_1, List)) and len(axis_1) == 2:
            axis_1, axis_2 = axis_1
            self.axis_1 = float(axis_1)
            self.axis_2 = float(axis_2)
            setattr(self, name_1, axis_1)
            setattr(self, name_2, axis_2)
        else:
            self.axis_1 = getattr(axis_1, name_1, 0.0)
            self.axis_2 = getattr(axis_1, name_2, 0.0)
        super().__init__([self.axis_1, self.axis_2])

    @staticmethod
    def _v(vector) -> "StdVector2":
        if isinstance(vector, StdVector2):
            return vector
        else:
            from ts4lib.classes.coordinates.std_vector3 import StdVector3
            from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
            if isinstance(vector, StdQuaternion) or isinstance(vector, StdVector3):
                return StdVector2(vector)
            else:
                return StdVector2()

    def __add__(self, vector: "StdVector2") -> "StdVector2":
        return StdVector2(*super().__add__(self._v(vector)))

    def __sub__(self, vector: "StdVector2") -> "StdVector2":
        return StdVector2(*super().__sub__(self._v(vector)))

    def __mul__(self, vector: "StdVector2") -> float:
        """
         :param vector: Std2DVector (or 3D or Q), otherwise Std2DVector(0, 0) will be used
        :return: The dot / scalar product
        """
        _vector = self._v(vector)
        return self.axis_1 * _vector.axis_1 + self.axis_2 * _vector.axis_2

    def dot(self, vector: "StdVector2") -> float:
        """ Deprecated, use 'self * vector' """
        return self * vector

    def scalar(self, vector: "StdVector2") -> float:
        """ Deprecated, use 'self * vector' """
        return self * vector

    def cross(self, vector: "StdVector2") -> float:
        """
        Calculate 'self × vector'
        :param vector: StdVector2 (or 3D or Q), otherwise StdVector2(0, 0) will be used
        :return: The value for the 3rd axis of a Std3DVector that is perpendicular (⦝) to the two vectors.
        """
        _vector = self._v(vector)
        axis_3 = self.axis_1 * _vector.axis_2 - _vector.axis_1 * self.axis_2
        return axis_3

    def cross_3d(self, vector: "StdVector2") -> "StdVector3":
        """
        Calculate 'self × vector'
        :param vector: StdVector2 (or 3D or Q), otherwise StdVector2(0, 0) will be used
        :return: A Std3DVector that is perpendicular (⦝) to the two vectors.
        """
        axis_3 = self.cross(vector)

        self._x = axis_3
        self._y = axis_3
        self._z = axis_3
        for axis_name in self.axis_names:
            if getattr(self, axis_name, None) is not None:
                setattr(self, f"_{axis_name}", 0.0)
        from ts4lib.classes.coordinates.std_vector3 import StdVector3
        return StdVector3(getattr(self, '_x'), getattr(self, '_y',), getattr(self, '_z'))

    def length(self) -> float:
        return math.sqrt(self.axis_1 ** 2 + self.axis_2 ** 2)

    def as_ts4_vector2(self):
        try:
            # noinspection PyUnresolvedReferences
            from sims4.math import Vector2, Quaternion, Transform, Location
            return Vector2(self.axis_1, self.axis_2)
        except:
            pass
        return None

    def randomize(self) -> "StdVector2":
        return StdVector2(*super().randomize())
