#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from ts4lib.classes.math.vector_interface import VectorInterface


class StdVector(VectorInterface):
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        """
        StdVector(x, y, z) - TS4 may handle axes differently
        :param x: x-axis to the right
        :param y: y-axis to the top
        :param z: z-axis to / from the viewer
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        super().__init__([self.x, self.y, self.z])
