# -*- coding: utf-8 -*-
"""
Indhu Cimbali Suresh
10478874
The primary goal of this file is to demonstrate a simple unittest implementation and
thorough testing of the classifyTriangle() function
"""

import unittest

from triangle_improved import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classify_triangle(60,61,11),'Right','420,421,30 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classify_triangle(1.5,1.5,1.5),'Equilateral','1.5,1.5,1.5 should be equilateral')

    def testEquilateralTrianglesC(self):
        self.assertEqual(classify_triangle(300,300,300),'Equilateral','300,300,300 should be equilateral')
    
    def testIsoscelesTrianglesA(self):
        self.assertEqual(classify_triangle(2,2,3),'Isosceles','2,2,3 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classify_triangle(8.9,8.9,12),'Isosceles','8.9,8.9,12 should be isosceles')

    def testIsoscelesTrianglesC(self):
        self.assertEqual(classify_triangle(400.25,400.25,500.1),'Isosceles','400.25,400.25,500.1 should be isosceles')

    def testScaleneTrianglesA(self):
        self.assertEqual(classify_triangle(4,5,6),'Scalene','4,5,6 should be scalene')

    def testScaleneTrianglesB(self):
        self.assertEqual(classify_triangle(3.4,5.6,7.8),'Scalene','3.4,5.6,7.8 should be scalene')

    def testScaleneTrianglesC(self):
        self.assertEqual(classify_triangle(250, 300, 350),'Scalene','250,300,350 should be scalene')

    def testInputsA(self):
        self.assertEqual(classify_triangle('a',[1,2,3],(1,2,3)),'InvalidInput','This function should only accept positive numbers')

    def testInputsB(self):
        self.assertEqual(classify_triangle(0,0,0),'InvalidInput','This function should only accept positive numbers')

    def testInputsC(self):
        self.assertEqual(classify_triangle(3,-4,5),'InvalidInput','This function should only accept positive numbers')

    def testInputsD(self):
        self.assertEqual(classify_triangle(-3,-4,-5),'InvalidInput','This function should only accept positive numbers')

    def testInputsE(self):
        self.assertEqual(classify_triangle(0,1,1),'InvalidInput','This function should only accept positive numbers')

    def testValidTrianglesA(self):
        self.assertEqual(classify_triangle(1,2,3),'NotATriangle','1,2,3 is not a valid triangle')

    def testValidTrianglesB(self):
        self.assertEqual(classify_triangle(4,4,400),'NotATriangle','4,4,400 is not a valid triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()