#
# LICENSE https://creativecommons.org/licenses/by/4.0/ https://creativecommons.org/licenses/by/4.0/legalcode
# © 2023 https://github.com/Oops19
#


from typing import Union, List, Tuple


class VectorInterface:
    """
    Generic tools for 2D, 3D and 4D (or even 5D) data like vectors, angles and quaternions.
    This class stores the data, allows comparison and representation of it.
    """
    def __init__(self, vector: Union[None, List[float]] = None):
        if vector:
            self._vector = vector
        else:
            self._vector = []

    @property
    def vector(self):
        return self._vector

    def __str__(self) -> str:
        """
        :return: Returns the vector formatted with the default parameters.
        """
        return self.format()

    def format(self, digits: int = 3, separator: str = ', ', left_str = '(', right_str = ')', multiplier: float = 1) -> str:
        """
        :param digits: The number of digits to use, default: 3
        :param separator: The separator between the values, default: ', '
        :param left_str: Prepend to the return string, default: '('
        :param right_str: Append to the return string, default: ')'
        :param multiplier: Set to '180 / math.pi' to get values in '°', otherwise 'rad' is returned.
        :return: A formatted vector in the form (1.123, 2.123, 3.123) with 1-n values depending on the vector length
        """
        rv = ''
        for i in range(0, len(self.vector)):
            if i == len(self.vector) - 1:
                rv += f"{multiplier * self.vector[i]:0.{digits}f}"
                break
            rv += f"{multiplier * self.vector[i]:0.{digits}f}{separator}"
        return f"{left_str}{rv}{right_str}"

    def __eq__(self, vector):
        """
        :param vector: Vector to compare to.
        :return: Returns 'True' if vectors are similar according to the default parameters.
        """
        return self.equals(vector)

    def equals(self, vector, tolerance: float = 0.001) -> bool:
        """
        :param vector: Vector to compare to.
        :param tolerance: The maximum tolerance both vectors are allowed to differ, default: 0.001
        :return: Returns 'True' if vectors are similar according to the tolerance.
        """
        delta: float = 0.0
        for i in range(0, len(self.vector)):
            delta += abs(self.vector[i] - vector.vector[i])

        if delta <= tolerance:
            return True
        return False

    def __iter__(self):
        for n in self._vector:
            yield n

    def as_list(self) -> List[float]:
        return list(n for n in self._vector)

    def as_tuple(self) -> Tuple[float]:
        return tuple(n for n in self._vector)
