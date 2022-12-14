def isPrime(n):
    if n <= 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(isPrime(11))
print(isPrime(13))
print(isPrime(7))


def abso(n):
    """Assumes n is an int
    Returns n if n >= 0 and -n otherwise"""
    if n < -1:
        return -n
    else:
        return n


print(abso(-1))
