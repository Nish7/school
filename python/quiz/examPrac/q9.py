#!/usr/bin/python3
import unittest

# --------------------------------------------------------------e136
# REVIEW: condition, loop, approximation, string, list, dict,
# recursion, 2d matrix, EXCEPTION, class
# --------------------------------------------------------------
def q9(s, insertionletter):
    """
    Assumes s is a string, and insertionletter is a letter.
    Returns a string obtained by inserting insertionletter
    between each pair of letters in s.
    Raises ValueError if the arguments are not as assumed.

    q9('blue', 'x') should return 'bxlxuxe'
    q9(529, 'x') should raise ValueError
    q9('red', 'yz') should raise ValueError
    q9('', 'z') should return ''
    q9('x', 'z') should return 'x'
    q9('zz', 'z') should return 'zzz'
    """
    if len(insertionletter) > 1 or type(s) != str:
        raise (ValueError())

    if len(s) == 0:
        return ""

    st = s[0]

    if len(s) > 1:
        for l in s[1:]:
            st += insertionletter + l
    else:
        st = s

    return st


# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(q9("blue", "x"), "bxlxuxe")

    def test2(self):
        with self.assertRaises(ValueError):
            q9(529, "x")

    def test3(self):
        with self.assertRaises(ValueError):
            q9("red", "xy")

    def test4(self):
        self.assertEqual(q9("y", "x"), "y")

    def test5(self):
        self.assertEqual(q9("", "x"), "")

    def test6(self):
        self.assertEqual(q9("xx", "x"), "xxx")


if __name__ == "__main__":
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
