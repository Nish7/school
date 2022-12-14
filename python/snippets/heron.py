# For finding the square root.


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
