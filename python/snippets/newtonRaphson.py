"""
 Newton-Raphson algorithm is to find the root of polynomial.
     - Given a guess g for the root. 
     - a better guess is g = g - p(g) / p'(g)
"""

# Apprach 1: Using a for loop
def newRap_1():
    # The polynomial Function
    def p(x, k):
        return x ** 2 - k

    # The derative function
    def dp(x):
        return 2 * x

    k = 24

    g = k / 2  # First guess for the square root.

    for i in range(10):
        g = g - p(g, k) / dp(g)


# Approach 2: Using a while loop
def newRap_2():
    # The polynomial Function
    def p(x, k):
        return x ** 2 - k

    # The derative function
    def dp(x):
        return 2 * x

    k = 24
    g = k / 2

    epsilon = 0.001

    while abs(g ** 2 - k) > epsilon:
        g = g - p(g, k) / dp(g)

    return g


# For cube root
def newRap_cube():
    # The polynomial Function
    def p(x, k):
        return x ** 3 - k

    # The derative function
    def dp(x):
        return 3 * (x ** 2)

    k = 27
    g = k / 2

    epsilon = 0.001

    while abs(g ** 3 - k) > epsilon:
        g = g - p(g, k) / dp(g)

    return g


# for n cube
def newRap_n(k, n, e=0.0001):
    # The polynomial Function
    def p(x, k):
        return x ** n - k

    # The derative function
    def dp(x):
        return n * (x ** (n - 1))

    g = k / 2

    while abs(g ** n - k) > e:
        g = g - p(g, k) / dp(g)

    return round(g, 4)
