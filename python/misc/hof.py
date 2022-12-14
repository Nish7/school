# Higher order functions
# List of some usefull function


# Note: These all are iterable and not lists, thats why i am converting to lists, when printing them

# 1. map
# Return a new function, and takes 2 main arguments which are function and iterable [list of itererable] and applies the function to every element in the list.
# --> [1, 4, 9, 16]

arr = [1, 2, 3, 4]


def square(x):
    return x ** 2


sqrs = map(square, arr)
print(sqrs)

# 2. zip
# returns a list with the each index with the tuple product of the both the lists [stops at the minimum length]
# --> [(5,3),(99, 100), (2, 9)]

L1 = [5, 99, 2]
L2 = [3, 100, 9, 10]

print(list(zip(L1, L2)))

# 4. enumerate
# enumerates the lists --> ['dog', 'foo', 'boo'] --> [(0, 'dog'), (1, 'foo'), (2, 'booo')]

arr = ["dog", "foo", "boo"]

list(enumerate(arr))
