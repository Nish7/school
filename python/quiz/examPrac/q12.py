#!/usr/bin/python3
import unittest

# --------------------------------------------------------------e128
# Review:CONDITION, loop, approx, string, list, dict, recursion, 2D, exception,
# class
#
# --------------------------------------------------------------
def q1(a, b, c, epsilon):
    """
    Returns True if a, b, c are all within epsilon of each other.
    For example,
    q1() is True
    q1() is False
    """

    if abs(c - a) > epsilon:
        return False
    elif abs(b - a) > epsilon:
        return False
    elif abs(b - c) > epsilon:
        return False

    return True

    pass


# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(q1(5, 6, 7, 2), True)

    def test1(self):
        self.assertEqual(q1(5, 6, 7, 1.5), False)

    def test2(self):
        self.assertEqual(q1(1, 2, 3, 1), False)

    def test3(self):
        self.assertEqual(q1(9, 9, 9, 0), True)

    def test4(self):
        self.assertEqual(q1(9, 9, 9, 100), True)

    def test5(self):
        self.assertEqual(q1(90, 90, 0, 0), False)


if __name__ == "__main__":
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
