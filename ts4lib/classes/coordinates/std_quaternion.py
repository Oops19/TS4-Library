#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import math
from typing import List, Any, Union, Tuple
from ts4lib.classes.coordinates.vector_interface import VectorInterface


class StdQuaternion(VectorInterface):
    """
    This 'Standard Quaternion' implementation uses the standard w, x, y, z notation. The TS4 implementation uses x, y, z, w.
    Expect the unexpected when confusing one or the other quaternion type or the order.
    Expect the unexpected when using quaternions which are not normalized.
    """

    def __init__(self, w: Union[Union[float, int, Tuple[Union[float, int], Union[float, int], Union[float, int], Union[float, int]], List[Union[float, int]]] , "StdQuaternion", "StdVector3", "StdVector2"] = 1.0, x: Union[float, int] = 0.0, y: Union[float, int] = 0.0, z: Union[float, int] = 0.0):
        """
        StdQuaternion(w, x, y, z)
        With no parameters supplied (1,0,0,0) 'identity quaternion' will be returned.
        @param w: float = w
        @param x: float = x
        @param y: float = y
        @param z: float = z

        @param x: Tuple, List will be treated as a wxyz quaternion
        @param w: StdQuaternion which will be converted to a StdQuaternion.
        @param w: Std3DVector which will be converted to a StdQuaternion.
        @param w: Std2DVector which will be converted to a StdQuaternion.
        @param w: The object needs the attributes 'w', 'x', 'y' and 'z' or they are set to 0.
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

    def normalize(self, tolerance: float = 0.00001) -> "StdQuaternion":
        mag2 = sum(n * n for n in self)
        if mag2 == 0:
            # Normalise a 0,0,0,0 quaternion to 1,0,0,0 (identity)
            return StdQuaternion()
        mag3 = abs(1 - mag2)
        if mag3 > tolerance:
            mag = math.sqrt(mag2)
            q = tuple(n / mag for n in self)
            return StdQuaternion(*q)
        return self

    def conjugate(self):
        """ :return: Conjugate """
        return StdQuaternion(self.w, -self.x, -self.y, -self.z)

    def __add__(self, quaternion: Any) -> "StdQuaternion":  # Union["StdQuaternion", "Std3DVector", "Std2DVector"]) -> "StdQuaternion":
        return StdQuaternion(*super().__add__(self._q(quaternion)))

    def add(self, quaternion: Any) -> "StdQuaternion":  # Union["StdQuaternion", "Std3DVector", "Std2DVector"]) -> "StdQuaternion":
        """ Normalized result for 'self + quaternion' """
        return (self + quaternion).normalize()

    def __sub__(self, quaternion: Any) -> "StdQuaternion":  # Union["StdQuaternion", "Std3DVector", "Std2DVector"]) -> "StdQuaternion":
        return StdQuaternion(*super().__sub__(self._q(quaternion)))

    def sub(self, quaternion: Any) -> "StdQuaternion":  # Union["StdQuaternion", "Std3DVector", "Std2DVector"]) -> "StdQuaternion":
        """ Normalized result for 'self - quaternion' """
        return (self + quaternion).normalize()

    def __mul__(self, quaternion: "StdQuaternion") -> "StdQuaternion":
        """
        Multiplies two quaternions without normalizing the result.  Use `q = q1 * q2` for a normalized result.
        :param quaternion: The 2nd quaternion or Quaternion(0, 3d-vector)
        :return: Product of  Quaternion, not normalized
        """
        w = self.w * quaternion.w - self.x * quaternion.x - self.y * quaternion.y - self.z * quaternion.z
        x = self.w * quaternion.x + self.x * quaternion.w + self.y * quaternion.z - self.z * quaternion.y
        y = self.w * quaternion.y - self.x * quaternion.z + self.y * quaternion.w + self.z * quaternion.x
        z = self.w * quaternion.z + self.x * quaternion.y - self.y * quaternion.x + self.z * quaternion.w
        return StdQuaternion(w, x, y, z)

    def multiply(self, quaternion: "StdQuaternion") -> "StdQuaternion":
        """ Normalized result for 'self * quaternion' """
        return (self * quaternion).normalize()

    def __truediv__(self, quaternion: "StdQuaternion") -> "StdQuaternion":
        """
        Divides two quaternions without normalizing the result. Use `q = q1 / q2` for a normalized result.
        :param quaternion: The 2nd quaternion or Quaternion(0, 3d-vector)
        :return: Quotient as Quaternion, not normalized
        """
        return self * quaternion.conjugate()

    def divide(self, quaternion):
        """ Normalized result for 'self / quaternion' """
        return (self / quaternion).normalize()

    def euler_angles(self) -> Any:  # "StdEulerAngle":
        roll, pitch, yaw = self.get_euler_angles()
        from ts4lib.classes.coordinates.std_euler_angle import StdEulerAngle
        return StdEulerAngle(roll, pitch, yaw)

    def get_euler_angles(self) -> List:
        """
        :return: StdEulerAngle, order roll, pitch, yaw; unit in 'rad'
        """
        sinr_cosp = 2 * (self.w * self.x + self.y * self.z)
        cosr_cosp = 1 - 2 * (self.x * self.x + self.y * self.y)
        roll = math.atan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (self.w * self.y - self.z * self.x)
        if abs(sinp) >= 1:
            pitch = math.copysign(math.pi / 2, sinp)  # // use +-90 degrees if out of range
        else:
            pitch = math.asin(sinp)

        siny_cosp = 2 * (self.w * self.z + self.x * self.y)
        cosy_cosp = 1 - 2 * (self.y * self.y + self.z * self.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        return [roll, pitch, yaw]

    def rotate_vector(self, vector: Union["StdVector3", "StdQuaternion"]) -> Any:
        """
        Usage: q.rotate_vector(v2) || q.rotate_vector(StdVector(q=q2)
        @param vector: StdVector3 - will be converted to a quaternion
        @param vector: StdQuaternion
        @return: StdVector
        """
        from ts4lib.classes.coordinates.std_vector3 import StdVector3
        if isinstance(vector, StdVector3):
            q = StdQuaternion(0, vector.x, vector.y, vector.z)  # convert vector (not euler angle) to quaternion
        else:
            q = vector
        q = (self * q) * self.conjugate()
        return StdVector3(q.x, q.y, q.z)

    def as_ts4_quaternion(self):
        try:
            # noinspection PyUnresolvedReferences
            from sims4.math import Vector3, Quaternion, Transform, Location
            return Quaternion(self.x, self.y, self.z, self.w)
        except:
            pass
        return None

    @staticmethod
    def _q(quaternion: Any) -> "StdQuaternion":
        if isinstance(quaternion, StdQuaternion):
            return quaternion
        else:
            from ts4lib.classes.coordinates.std_vector3 import StdVector3
            from ts4lib.classes.coordinates.std_vector2 import StdVector2
            if isinstance(quaternion, StdVector3) or isinstance(quaternion, StdVector2):
                return StdQuaternion(quaternion)
            else:
                return StdQuaternion()

    def randomize(self) -> "StdQuaternion":
        return StdQuaternion(*super().randomize())
