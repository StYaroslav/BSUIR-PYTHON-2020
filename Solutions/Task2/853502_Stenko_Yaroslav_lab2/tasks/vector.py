class Vector:

    def __init__(self, *nums):
        self.array = list(nums)

    def __repr__(self):
        repr_string = ''
        repr_string += '['
        for i in self.array:
            repr_string += '{}, '.format(str(i))
        repr_string = repr_string[:-2]
        repr_string += ']'
        return repr_string

    def __getitem__(self, item):
        if item < len(self.array):
            return self.array[item]
        else:
            raise IndexError

    def __len__(self):
        return len(self.array)

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.__len__() == other.__len__():
                return [v + w for v, w in zip(self.array, other)]
            else:
                raise DimensionError
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            if self.__len__() == other.__len__():
                return [v - w for v, w in zip(self.array, other)]
            else:
                raise DimensionError
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return [v * other for v in self.array]
        else:
            if self.__len__() == other.__len__():
                return sum(v * w for v, w in zip(self.array, other))
            else:
                raise DimensionError

    def __eq__(self, other):
        return all([v == w for v, w in zip(self.array, other)])


class DimensionError(Exception):
    pass