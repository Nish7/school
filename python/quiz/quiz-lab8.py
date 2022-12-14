# factorial --> n*(n-1)*(n-2)...


def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))
