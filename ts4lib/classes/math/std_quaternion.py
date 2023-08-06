#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


import math
from typing import List

from ts4lib.classes.math.std_vector import StdVector
from ts4lib.classes.math.vector_interface import VectorInterface


class StdQuaternion(VectorInterface):
    """
    This 'Standard Quaternion' implementation uses the standard w, x, y, z notation. The TS4 implementation uses x, y, z, w.
    Expect the unexpected when confusing one or the other quaternion type or the order.
    Expect the unexpected when using quaternions which are not normalized.
    """
    def __init__(self, w: float, x: float, y: float, z: float):

        if x == 0 and y == 0 and z == 0:
            self.w = 1.0
        else:
            self.w = float(w)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        super().__init__([self.w, self.x, self.y, self.z])

    def normalize(self, tolerance: float = 0.00001):
        mag2 = sum(n * n for n in self) #
        mag3 = abs(1 - mag2)
        if mag3 > tolerance:
            mag = math.sqrt(mag2)
            q = tuple(n / mag for n in self)
            return StdQuaternion(q[0], q[1], q[2], q[3])
        return self

    def conjugate(self):
        """ :return: Conjugate """
        return StdQuaternion(self.w, -self.x, -self.y, -self.z)

    def __truediv__(self, quaternion):
        return (self.divide(quaternion)).normalize()

    def divide(self, quaternion):
        """
        Divides two quaternions without normalizing the result. Use `q = q1 / q2` for a normalized result.
        :param quaternion: The 2nd quaternion or Quaternion(0, 3d-vector)
        :return: Quotient as Quaternion, not normalized
        """
        return self.multiply(quaternion.conjugate())

    def __mul__(self, quaternion):
        return self.multiply(quaternion).normalize()

    def multiply(self, quaternion):
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

    def get_euler_angles(self) -> List[float]:
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

    def rotate_vector(self, vector: StdVector) -> StdVector:
        _vector = StdQuaternion(0, vector.x, vector.y, vector.z)  # convert vector (not euler angle) to quaternion
        q = self.multiply(_vector).multiply(self.conjugate())  # q.w will be zero.
        return StdVector(q.x, q.y, q.z)

    def as_ts4_quaternion(self):
        try:
            # noinspection PyUnresolvedReferences
            from sims4.math import Vector3, Quaternion, Transform, Location
            return Quaternion(self.x, self.y, self.z, self.w)
        except:
            pass
        return None
