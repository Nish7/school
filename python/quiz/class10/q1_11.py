#!/usr/bin/python3
import unittest

# -------------------------------------------------
# Fill this in:  (replace the underscores with your information)
# Student Last Name: Kapadia
# Student First Name: Nishil
# Student Number: 501080772
# Ryerson email: n1kapadia@ryerson.ca
# --------------------------------------------------------------
# Hello World
# --------------------------------------------------------------
def hello():
    """
    The Doc string (in triple quotes) tells what to do and what
    to assume.  In this case, we assume that you have filled in
    the student information above.
    This function should return (NOT PRINT): "Hello World"
    Your job is to replace the pass-statement with code that
    achieves the goal of the function.  When you run the Python file
    the the unittests will give you an indication of whether your
    code is doing what it should.
    """
    return "Hello World"


# --------------------------------------------------------------
# The Testing
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(hello(), "Hello World")


if __name__ == "__main__":
    unittest.main(exit=True)


# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
