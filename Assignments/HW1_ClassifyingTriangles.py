import unittest

def classify_triangle(a,b,c):
    if (a == b and a == c):
        return ("Equilateral")
    elif (a**2 + b**2 == c**2):
        return ("Right")
    elif (a != b and a != c and b != c):
        return ("Scalene")
    else:
        return ("Isosceles")
    
class TestTriangles(unittest.TestCase):
    def testEquilateral(self): # test Equilateral triangle inputs
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 is an Equilateral triangle')
        self.assertEqual(classify_triangle(2,2,2),'Equilateral','2,2,2 is an Equilateral triangle')
        self.assertNotEqual(classify_triangle(3,3,4),'Equilateral','3,3,4 is NOT an Equilateral triangle')

    def testRight(self): # test Right triangle inputs
        self.assertEqual(classify_triangle(3,4,5), 'Right', '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(10,24,26), 'Right', '10,24,26 is a Right triangle')
        self.assertNotEqual(classify_triangle(3,4,4), 'Right', '3,4,4 is a NOT Right triangle')
    
    def testScalene(self): # test Scalene triangle inputs
        self.assertEqual(classify_triangle(1,2,3), 'Scalene', '1,2,3 is a Scalene triangle')
        self.assertEqual(classify_triangle(4,5,6), 'Scalene', '4,5,6 is a Scalene triangle')
        self.assertNotEqual(classify_triangle(6,7,7), 'Scalene', '3,4,8 is NOT a Scalene triangle')

    def testIsosceles(self): # test Isosceles triangle inputs 
        self.assertEqual(classify_triangle(1,2,2), 'Isosceles', '1,2,2 is an Isosceles triangle')
        self.assertEqual(classify_triangle(2,3,3), 'Isosceles', '2,3,3 is an Isosceles triangle')
        self.assertNotEqual(classify_triangle(3,4,6), 'Isosceles', '3,4,4 is NOT an Isosceles triangle')


if __name__ == "__main__":
    unittest.main()
