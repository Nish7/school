#!/usr/bin/python3
import unittest
from matrices import *

# --------------------------------------------------------------q2.py
# Two-dimensional arrays, simple algorithms
# --------------------------------------------------------------

# --------------------------------------------------------------
# Find the number of values in the matrix that ...
# --------------------------------------------------------------
def count23(matrix):
    """
    Returns the number of values in the matrix that
    are divisible by both 2 and 3
    """
    count = 0
    for i in matrix:
        for y in i:
            if y % 2 == 0 and y % 3 == 0:
                count += 1

    return count


# ----------------------------------------------------------
# Show the matrices that we imported
# matrix1, matrix2 and using printmx()
# --------------------------------------------------------------
printmx(matrix1)
printmx(matrix2)
printmx(matrix3)
printmx(matrix4)
printmx(matrix5)
# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(count23(matrix1), 6)

    def test2(self):
        self.assertEqual(count23(matrix2), 5)

    def test3(self):
        self.assertEqual(count23(matrix3), 20)

    def test4(self):
        self.assertEqual(count23(matrix4), 16)

    def test5(self):
        self.assertEqual(count23(matrix5), 0)


if __name__ == "__main__":
    unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
