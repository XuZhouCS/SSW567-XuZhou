# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""


def classify_triangle(edge1, edge2, edge3):
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

    if not all(isinstance(x, int) for x in [edge1, edge2, edge3]):
        return 'NotATriangle'
    if edge1 <= 0 or edge2 <= 0 or edge3 <= 0:
        return 'NotATriangle'
    if not edge1 + edge2 > edge3 or not edge2 + edge3 > edge1 or not edge1 + edge3 > edge2:
        return 'NotATriangle'

    edge1, edge2, edge3 = sorted([edge1, edge2, edge3])
    if edge1 == edge2 and edge2 == edge3:
        return 'Equilateral'
    if edge1 == edge2 or edge2 == edge3 or edge1 == edge3:
        return 'Isoceles'
    if edge1**2 + edge2**2 == edge3**2:
        return 'Right'

    return 'Scalene'


print(classify_triangle(3, 4, 5))
