def perfectcube(n):
    """
    Write a function perfectcube(n), which returns True if n is a perfect cube and returns False
    otherwise. Notice that this function is not printing anything, but rather returning True or False.
    The function must use exhaustive enumeration to check if n is a perfect cube. That means
    checking if 0**3 is n or 1**3 is n or 2**3 is n, and so on, up to where it is pointless to check
    further. (Instead of n, you might be checking against abs(n), since for example, -125 is a perfect
    cube.
    """
    n = abs(int(n))

    for i in range(n):
        if i ** 3 == n:
            return True

    return False
