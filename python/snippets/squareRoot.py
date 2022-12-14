def squareRoot(x, epsilon):
    """
    Write a function squareRoot(x, epsilon) that uses bisection search to return a number y that is
    close enough to the square root of x, so that abs(y**2 - x) < epsilon. Try out the function in a
    program to verify that it works properly
    """

    n = int(x)
    epsilon = float(epsilon)

    while n <= 0:
        n = int(input("Input a positive number:"))

    max = n
    min = 0

    while True:
        mid = (max + min) / 2
        sqr = mid ** 2

        if abs(n - sqr) <= epsilon:
            return round(mid, 5)
        elif sqr > n:
            max = mid
        elif sqr < n:
            min = mid
