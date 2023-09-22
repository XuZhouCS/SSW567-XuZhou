import pytest
from HW01.classify import classify_triangle


def test_classify_triangle():
    triangles = [
        [1, 2, 3, 'Not a triangle'],
        [1, 1, 1, 'Equilateral Triangle'],
        [3, 3, 2, 'Isosceles Triangle'],
        [3, 4, 5, 'Scalene and Right Triangle'],
        [5, 4, 3, 'Scalene and Right Triangle'],
        [-1, 2, 3, 'All sides must be greater than 0'],
        [0, 2, 3, 'All sides must be greater than 0'],
        ['a', 2, 3, 'All sides must be integers'],
        ['1', 2, 3, 'All sides must be integers'],
    ]

    for a, b, c, expected in triangles:
        print(a, b, c, expected)
        assert classify_triangle(a, b, c) == expected
