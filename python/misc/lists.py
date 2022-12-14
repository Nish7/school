# Lists
# Lists are mutable

arr = []

# --- Operations ---

# Add Method: Mutates
arr.append(12)

# Extend : Mutates
arr.extend([1, 3])

# Delete element
del arr[2]

# Remove last element and returns the last element: default to -1 and index can be changes
del_el = arr.pop()

# Remove a specific element
del_el = arr.remove(12)

# Split the string to list
"a b c d e".split(" ")  # --> ['a', 'b', ...]

# Join Lists
"".join(["as", "12"])  # --> 'as12' --> string

# Reverse
arr.reverse()

# Sorted and Sort
# Sort: with a comporator function - mutates the list and sorted without the comparotor function - returns a new list
arr.sorted()

# --- Range ---
# Range is a immutable, iterable and generator function
# can be converted to a list using list(range(1, 10))

# ---- Memory, Aliases and pointers ----
evens = [2, 4, 6]
odd = [1, 3, 5]
numbers = [evens, odd, "not a number"]  # --> [[2, 4, 6], [1, 3, 5]]

# its stil points towards its original object's address
numbers[0] is evens  # --> True
numbers[1] is odd  # --> True

# If you mutate the original object, the number would change aswell.
# These are called ALIASES
evens.append(8, 10)
print(numbers)  # --> [[2,4, 6, 8,10], [1, 3, 5]]

# These are aliases aswell
zeros = [0] * 50

# ---- Cloning ----
chill = numbers[:]  # --> Shallow copy
