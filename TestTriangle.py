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
        self.assertEqual(classifyTriangle(3,4,5),'Right')
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(8,6,10),'Right')
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(12,5,13),'Right')
    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(7,24,25),'Right')
    def testRightTriangleE(self):
        self.assertEqual(classifyTriangle(5,3,4),'Right')

        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(6,6,6), 'Equilateral')
    def testEquilateralTrianglesC(self): 
        self.assertEqual(classifyTriangle(10,10,10), 'Equilateral')
    def testEquilateralTrianglesD(self): 
        self.assertEqual(classifyTriangle(100,100,100), 'Equilateral')
    def testEquilateralTrianglesE(self): 
        self.assertEqual(classifyTriangle(75,75,75), 'Equilateral')

    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(1,2,2),'Isosceles')
    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(4,4,6),'Isosceles')
    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(5,3,3),'Isosceles')
    def testIsoscelesTrianglesD(self):
        self.assertEqual(classifyTriangle(11,3,11),'Isosceles')
    def testIsoscelesTrianglesE(self):
        self.assertEqual(classifyTriangle(60,60,70),'Isosceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classifyTriangle(8,16,10),'Scalene')
    def testScaleneTrianglesB(self):
        self.assertEqual(classifyTriangle(13,11,10),'Scalene')
    def testScaleneTrianglesC(self):
        self.assertEqual(classifyTriangle(9,17,11),'Scalene')
    def testScaleneTrianglesD(self):
        self.assertEqual(classifyTriangle(7,9,3),'Scalene')
    def testScaleneTrianglesE(self):
        self.assertEqual(classifyTriangle(18,16,7),'Scalene')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-8,6,6), 'InvalidInput')
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-7,-4,-6), 'InvalidInput')
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(201,6,6), 'InvalidInput')
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(600,700,800), 'InvalidInput')
    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(0,0,0), 'InvalidInput')
    def testInvalidInputF(self):
        self.assertEqual(classifyTriangle("0",0,0), 'InvalidInput')
    def testInvalidInputG(self):
        self.assertEqual(classifyTriangle("3","4","5"), 'InvalidInput')


    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(9,9,100), 'NotATriangle')
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(30,2,1), 'NotATriangle')
    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(16,1,1), 'NotATriangle')
    def testNotATriangleD(self):
        self.assertEqual(classifyTriangle(19,99,20), 'NotATriangle')
    def testNotATriangleE(self):
        self.assertEqual(classifyTriangle(1,1,3), 'NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

