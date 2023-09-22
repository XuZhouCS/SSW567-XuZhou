# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5),
                         'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4),
                         'Right', '5,3,4 is a Right triangle')

    def testEquilateralTriangles(self):
        self.assertEqual(classifyTriangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3),
                         'NotATriangle', '1,2,3 is not a triangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle('1', 2, 5),
                         'NotATriangle', '"1",2,5 is not a triangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1, 2, -1),
                         'NotATriangle', '1,2,-1 is not a triangle')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 2),
                         'Isoceles', '1,2,2 is an isoceles triangle')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(2, 1, 2),
                         'Isoceles', '2,1,2 is an isoceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(5, 6, 7),
                         'Scalene', '5,6,7 is a scalene triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
