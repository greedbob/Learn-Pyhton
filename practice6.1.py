# Question:第六章 练习一 给Point类增加方法
# Solution:
# Answer:

"""
This module provides the Point class.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True
"""

import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin()
        5.0
        """
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    def __add__(self, other):
        """sum x and y of two points separately

        >>> p = Point(1, 2) + Point(3, 4)
        >>> p
        Point(4, 6)
        """
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        """

        :param other:
        :return:
        """
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __itruediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)

    def __ifloordiv__(self, other):
        self.x //= other.x
        self.y //= other.y
        return self


if __name__ == "__main__":
    import doctest
    doctest.testmod()
