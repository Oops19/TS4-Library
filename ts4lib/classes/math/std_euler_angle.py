import math
#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.classes.math.vector_interface import VectorInterface


class StdEulerAngle(VectorInterface):
    def __init__(self, roll: float = 0, pitch: float = 0, yaw: float = 0):
        """
        StdEulerAngle(roll, pitch, yaw) - TS4 may handle axes differently
        :param roll: x-axis rotation in rad (axis to the right)
        :param pitch: y-axis rotation in rad (axis to the top)
        :param yaw: z-axis rotation in rad (axis to the viewer)
        """
        self.roll = float(roll)
        self.pitch = float(pitch)
        self.yaw = float(yaw)
        super().__init__([self.roll, self.pitch, self.yaw])

    def get_quaternion(self) -> list:
        cy = math.cos(self.yaw * 0.5)
        sy = math.sin(self.yaw * 0.5)
        cp = math.cos(self.pitch * 0.5)
        sp = math.sin(self.pitch * 0.5)
        cr = math.cos(self.roll * 0.5)
        sr = math.sin(self.roll * 0.5)

        w = cr * cp * cy + sr * sp * sy
        x = sr * cp * cy - cr * sp * sy
        y = cr * sp * cy + sr * cp * sy
        z = cr * cp * sy - sr * sp * cy
        return [w, x, y, z]

    def cross_prod(self, vector):
        return StdEulerAngle(
            self.pitch * vector.yaw - self.yaw * vector.pitch,
            self.yaw * vector.roll - self.roll * vector.yaw,
            self.roll * vector.pitch - self.pitch * vector.roll)

    def __mul__(self, vector):
        return StdEulerAngle(
            self.roll * vector.roll,
            self.pitch * vector.pitch,
            self.yaw * vector.yaw)
