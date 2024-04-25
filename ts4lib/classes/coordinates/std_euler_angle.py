#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19
#


import math
from typing import Any, Union, Tuple, List

from ts4lib.classes.coordinates.vector_interface import VectorInterface


class StdEulerAngle(VectorInterface):
    def __init__(self, roll: Union[float, int, Tuple[Union[float, int], Union[float, int], Union[float, int]], List[Union[float, int]]] = 0.0, pitch: Union[float, int] = 0.0, yaw: Union[float, int] = 0.0, convert_deg_to_rad: bool = False):
        """
        StdEulerAngle(roll, pitch, yaw) - TS4 may handle axes differently or use a different rotation order.
        @param roll: Tuple, the three float elements  will be treated as Roll, Pitch, Yaw
        @param roll: z-axis rotation in rad (z-axis to the viewer)
        @param pitch: x-axis rotation in rad (x-axis to the right)
        @param yaw: y-axis rotation in rad (y-axis to the top)

        @param convert_deg_to_rad: bool - Set to True if the supplied angles are in deg. All text output will be in deg.
        """
        if convert_deg_to_rad:
            factor = math.pi / 180
        else:
            factor = 1.0
        if (isinstance(roll, Tuple) or isinstance(roll, List)) and len(roll) == 3:
            roll, pitch, yaw = roll

        self.roll = float(roll * factor)
        self.pitch = float(pitch * factor)
        self.yaw = float(yaw * factor)
        super().__init__([self.roll, self.pitch, self.yaw])
        self.convert_to_deg = convert_deg_to_rad

    def quaternion(self) -> Any:  # "StdQuaternion":
        """
        @return: StdQuaternion
        """
        cy = math.cos(self.roll * 0.5)
        sy = math.sin(self.roll * 0.5)
        cp = math.cos(self.yaw * 0.5)
        sp = math.sin(self.yaw * 0.5)
        cr = math.cos(self.pitch * 0.5)
        sr = math.sin(self.pitch * 0.5)

        w = cr * cp * cy + sr * sp * sy
        x = sr * cp * cy - cr * sp * sy
        y = cr * sp * cy + sr * cp * sy
        z = cr * cp * sy - sr * sp * cy

        from ts4lib.classes.coordinates.std_quaternion import StdQuaternion
        return StdQuaternion(w, x, y, z)

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

    def rad(self) -> str:
        """
        :return: Returns the vector formatted with the default parameters.
        """
        return super().format(unit='', digits=3, multiplier=1)

    def deg(self) -> str:
        """
        :return: Returns the vector formatted with the default parameters.
        """
        return super().format(unit='°', digits=1, multiplier=180 / math.pi)
