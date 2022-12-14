#!/usr/bin/python3
import unittest

# --------------------------------------------------------------
# Heron Method for finding square root
# --------------------------------------------------------------
def heron(x, epsilon):
    """
    Assume that x and epsilon are positive numbers.
    Apply Heron's method to find a number g such that
    g ** 2 is within epsilon of x.  In other words, g is
    approximately the square root of x.
    This function should return g.
    For example, heron(25, 0.0001) might return 5.0000000001
    """
    guess = x

    while True:
        sqr = guess ** 2

        if epsilon >= abs(sqr - x):
            return guess
        else:
            guess = (guess + (x / guess)) / 2


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        x = 25
        eps = 0.0001
        self.assertAlmostEqual(heron(x, eps) ** 2, x, delta=eps)

    def test2(self):
        x = 250
        eps = 1
        self.assertAlmostEqual(heron(x, eps) ** 2, x, delta=eps)

    def test3(self):
        x = 0
        eps = 0.0001
        self.assertAlmostEqual(heron(x, eps) ** 2, x, delta=eps)

    def test4(self):
        x = 1000
        eps = 0.0000001
        self.assertAlmostEqual(heron(x, eps) ** 2, x, delta=eps)


if __name__ == "__main__":
    unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
