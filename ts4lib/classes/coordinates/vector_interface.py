#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2024 https://github.com/Oops19


import math
import random
from typing import Union, List, Tuple, Any, Dict


class VectorInterface:
    """
    Generic tools for 2D, 3D and 4D (or even 5D) data like vectors, angles and quaternions.
    This class stores the data, allows comparison and representation of it.
    Angles are stored in 'rad'. Set the property 'convert_to_deg' to 'True' to print angles in deg.
    """
    def __init__(self, vector: Union[None, List[float], Tuple[float, ...]] = None):
        if vector:
            self._vector = vector
        else:
            self._vector = []
        self._convert_to_deg = False

    @property
    def name(self) -> str:
        return 'VectorInterface'

    @property
    def vector(self):
        return self._vector

    @property
    def convert_to_deg(self) -> bool:
        return self._convert_to_deg

    @convert_to_deg.setter
    def convert_to_deg(self, convert_to_deg: bool):
        self._convert_to_deg = convert_to_deg

    def __str__(self) -> str:
        """
        :return: Returns the vector formatted with the default parameters.
        """
        return self.format()

    def __repr__(self) -> str:
        """
        :return: Returns the vector formatted with the default parameters.
        """
        return self.format()

    def _format(self, value: float, digits: int = 3):
        return f"{value:.{digits}f}".rstrip('0').rstrip('.')

    def format(self, digits: int = 3, unit: str = None, separator: str = ', ', left_str: str = '(', right_str: str = ')', multiplier: float = None, keep_trailing_zero: bool = False) -> str:
        """
        :param digits: The number of digits to use, default: 3
        :param unit: '', '°' or ' m'
        :param separator: The separator between the values, default: ', '
        :param left_str: Prepend to the return string, default: '('
        :param right_str: Append to the return string, default: ')'
        :param multiplier: Set to '180 / math.pi' to get values in '°', otherwise 'rad' is returned.
        @param: keep_trailing_zero: Set to True to get '1.000' instead of '1'
        :return: A formatted vector in the form (1.123, 2.123, 3.123) with 1-n values depending on the vector length
        """
        if self._convert_to_deg is True:
            if multiplier is None:
                multiplier = 180 / math.pi
            if unit is None:
                unit = f"°"
        if multiplier is None:
            multiplier = 1.0
        if unit is None:
            unit = ''

        rv: List[str] = []
        rv.append(f"{left_str}")
        for i in range(0, len(self.vector)):
            if keep_trailing_zero:
                rv.append(f"{(multiplier * self.vector[i]):0.{digits}f}{unit}")
            else:
                rv.append(f"{self._format(multiplier * self.vector[i], digits)}{unit}")
            if i != len(self.vector) - 1:
                rv.append(f"{separator}")
        rv.append(f"{right_str}")
        return ''.join(rv)

    def __eq__(self, vector):
        """
        :param vector: Vector to compare to.
        :return: Returns 'True' if vectors are similar according to the default parameters.
        """
        return self.equals(vector)

    def delta(self, vector) -> float:
        delta_vector = self - vector
        return sum(abs(i) for i in delta_vector)

    def equals(self, vector, tolerance: float = 0.001) -> bool:
        """
        :param vector: Vector to compare to.
        :param tolerance: The maximum tolerance both vectors are allowed to differ, default: 0.001
        :return: Returns 'True' if vectors are similar according to the tolerance.
        """

        delta = self.delta(vector)
        if delta <= tolerance:
            return True
        return False

    def __iter__(self):
        for n in self._vector:
            yield n

    def as_list(self) -> List[float]:
        return list(n for n in self._vector)

    def as_tuple(self) -> Tuple[float, ...]:
        return tuple(n for n in self._vector)

    def __sub__(self, vector: Any) -> Union[Any, None]:
        """
        :param vector: Vector to subtract. Supported types: StdQuaternion, StdVector
        :return: Returns the difference or throws an exception if the types don't match.
        """
        return [a - b for a, b in zip(self, vector)]

    def __add__(self, vector: Any) -> Union[Any, None]:
        """
        :param vector: Vector to add. Supported types: StdQuaternion, StdVector
        :return: Returns the sum or throws an exception if the types don't match.
        """
        return [a + b for a, b in zip(self, vector)]

    def randomize(self) -> "VectorInterface":
        """ Randomize vector values in the range [-w..w], [-x..x], [-y..y], [-z..z]
        'randomize()' should be implemented by StdVector / StdQuaternion to return the proper type
        Usage:
        * StdVector v = StdVector(*v._randomize())
        * StdQuaternion q = StdQuaternion(*q._randomize())
        """
        for i in range(0, len(self.vector)):
            self.vector[i] = random.random() * self.vector[i] * 2 - self.vector[i]
        return VectorInterface(self.vector)

    def magnitude(self) -> float:
        """ Return the length of the vector """
        return math.sqrt(sum(i ** 2 for i in self))

    def length(self) -> float:
        """ Return the length of the vector """
        return self.magnitude()

    def serialize(self) -> Dict[str, Tuple[float, ...]]:
        _, _, name = self.__module__.partition('.coordinates.')  # drop 'ts4lib.classes.coordinates.' and save 'xxx'
        name = f"{name}.{self.__class__.__name__}"
        return {name: self.as_tuple()}

    @classmethod
    def deserialize(cls, data: Dict[str, Tuple[float, ...]]) -> Any:
        import importlib
        prefix, coord, _ = cls.__module__.partition('.coordinates.')
        for name, values in data.items():
            _module_name, _class_name = name.rsplit('.', 1)
            _class = getattr(importlib.import_module(f"{prefix}{coord}{_module_name}"), _class_name)
            return _class(*values)
