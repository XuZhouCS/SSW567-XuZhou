# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classifyTriangle(a, b, c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 

    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """

    if not all(isinstance(x, int) for x in [a, b, c]):
        return 'NotATriangle'
    if a <= 0 or b <= 0 or c <= 0:
        return 'NotATriangle'
    if not a + b > c or not b + c > a or not a + c > b:
        return 'NotATriangle'

    a, b, c = sorted([a, b, c])
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isoceles'
    elif a**2 + b**2 == c**2:
        return 'Right'
    else:
        return 'Scalene'


print(classifyTriangle(3, 4, 5))
