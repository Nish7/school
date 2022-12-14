# Write a function that accepts one integer (30 by default) and computes all perfect squares less than or equal to the integer.
# The function should return a tuple/list of these perfect squares and how many of the perfect squares are divisble by 3 as two seperate variable


def perfectSquare(n):
    n = abs(int(n))

    # Loop through every number from 1 to n, check if its perfect square
    for i in range(1, n + 1):
        if i ** 2 == n:
            return True

    return False


def somesquares(n=30):
    sqr = []

    # Perfect square
    for i in range(1, n + 1):
        if perfectSquare(i):
            sqr.append(i)

    # Check if its divisble by 3
    modThree = 0
    for y in sqr:
        if y % 3 == 0:
            modThree += 1

    return (tuple(sqr), modThree)


print(somesquares())
print(somesquares(60))
