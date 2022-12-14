#!/usr/bin/python3
import unittest

# --------------------------------------------------------------e129
# Review: condition, LOOP, approx, string, list, dict, recursion, 2D, exception,
# class
# --------------------------------------------------------------
def q2(n):
    """
    Assumes n is an integer greater than or equal to 0.
    Returns the sum of the odd numbers from n to 3n, inclusive
    q2(2) returns 8  since 2, 3, 4, 5, 6  contains 3 and 5
    """
    ls = [i for i in range(n, (3 * n) + 1) if i % 2 != 0]
    return sum(ls)


# --------------------------------------------------------------
# Try it out:
# --------------------------------------------------------------
print(q2(2), "Expect 8")


class myTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(q2(2), 8)

    def test1(self):
        self.assertEqual(q2(10), 200)

    def test2(self):
        self.assertEqual(q2(0), 0)

    def test3(self):
        self.assertEqual(q2(100), 20000)


if __name__ == "__main__":
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
