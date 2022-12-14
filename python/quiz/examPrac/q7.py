#!/usr/bin/python3
import unittest

# --------------------------------------------------------------e134
# REVIEW: condition, loop, approximation, string, list, dict,
# RECURSION, 2D, exception, class
# --------------------------------------------------------------
def q7(s):
    """
    Assumes s is a string that has no punctuation and no blanks
    and is all lowercase.
    Returns True if s is a palindrome, False otherwise.

    You must use RECURSION to solve the problem.

    For example,
    q7('racecar') is True
    q7('blue') is False
    """

    if len(s) < 2:
        return True

    if s[0] != s[-1]:
        return False

    return q7(s[1:-1])


# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(q7("racecar"))

    def test2(self):
        self.assertFalse(q7("blue"))

    def test3(self):
        self.assertTrue(q7("madam"))


if __name__ == "__main__":
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
