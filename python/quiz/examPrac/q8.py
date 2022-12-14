#!/usr/bin/python3
import unittest

# --------------------------------------------------------------e135
# REVIEW: condition, loop, approximation, string, list, dict,
# recursion, 2D MATRIX, exception, class
# --------------------------------------------------------------
def q8(matrix):
    """
    Assumes that matrix is a 2D array of integers.
    Returns True if no number that occurs in the first row occurs
    any any other row.
    For example,
    q8([
    [5, 6, 7, 2],
    [9, 8, 4, 22]])   is True
    q8([
    [5, 6, 7, 2],
    [9, 8, 4, 22],
    [34, 1, 6, 99]])   is False since 6 from first row is in last row.
    """

    r_0 = matrix[0]

    for v in r_0:
        for r in matrix[1:]:
            for c in r:
                if c == v:
                    return False

    return True


# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        m = [[5, 6, 7, 2], [9, 8, 4, 22]]
        self.assertTrue(q8(m))

    def test2(self):
        m = [[5, 6, 7, 2], [9, 8, 4, 22], [34, 1, 6, 99]]
        self.assertFalse(q8(m))


if __name__ == "__main__":
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
