# Define a function that does the following:
# - Accepts two lists with the same length as parameters between elements from the first and second list
# - Unless the two element are the same
# - In the case that two elements are the same, insert this single element into the list.


# l1 and l2 are lists and of same length
def intersperse(l1, l2):
    res = []

    for i in range(len(l1)):
        # Check if the element is the same on the same index.
        if l1[i] == l2[i]:
            # then, prioritise l1 and append the element
            res.append(l1[i])
        else:
            # If not append, both the elements of same index from the lists
            res.append(l1[i])
            res.append(l2[i])

    return res


print(intersperse([1, 3, 5], [2, 4, 6]))
print(intersperse([1, 2, 3, 4], [1, 5, 6, 7]))
print(intersperse([1, 2, 3], [1, 2, 3]))
