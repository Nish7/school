# Tuple
# Main Reason - Mutability
# a list can be converted to a tuple using tuple() function

# How to append to a tuple without a list

# Fundamentlally: use the concentation of the two tuples,
# Caveat: you cannot concatinate tuples if one of the tuple have only one items.
# so you have add , after the first item.

a = (5, 92, 3)
b = ("abc",)
c = a + b
print(c)


# Intersect
def intersect(t1, t2):
    """Assume t1, t2 are tuples.
    Return a tuple of the common elements"""
    result = ()
    for element in t1:
        if element in t2 and element not in result:
            result = result + (element,)
    return tuple(sorted(result))
    pass


# ----------------------------------------------------
# Would intersect(t1, t2) be the same as intersect(t2, t1)?
# ----------------------------------------------------
t1 = (1, 2, 3, 3)
t2 = (3, 2, 4, 4, 2)
intersection12 = intersect(t1, t2)
intersection21 = intersect(t2, t1)
print(intersection12)
print(intersection21)
print("intersection12 and intersection21 are ", end=" ")

if intersection12 == intersection21:
    print("equal")
else:
    print("not equal")
print("-------------------")
