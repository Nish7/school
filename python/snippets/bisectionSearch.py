# Bisection Search
def bisectionSearch():
    """
    Write a program that uses bisection search to find the cube root of a number, where the number
    can be negative or positive.
    """

    n = int(input("Input a number:"))

    abs_n = abs(n)
    max = abs_n
    min = 0
    epsilon = 0.0001
    ans = ""

    while True:
        mid = (max + min) / 2
        cb = mid ** 3

        if abs(abs_n - cb) <= epsilon:
            ans = round(mid, 5)
            break
        elif cb > abs_n:
            max = mid
        elif cb < abs_n:
            min = mid

    if n < 0:
        return float("-" + str(ans))
    else:
        return float(ans)
