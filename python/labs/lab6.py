"""
@Title: Lab 6
@Author - Nishil K. - 501080772 - Section 01
@Deadline - 3rd Nov 
@Note: 'This file can be converted into .py'
"""

# 1. Write a program that has a loop to read in ten strings and put them into a list.
# Write a second loop to print the strings in the reverse order. This is an exercise in indexing,
# so do not use the reverse() method of list. Print the index in the following format. The actual
# strings you read in are arbitrary
def question_1():
    arr = []

    for i in range(10):
        inp = input(f"Enter the string ({i})/10: ")
        arr.append(inp)

    for y in range(10, 0, -1):
        print(f"String {y - 1}/10: {arr[y - 1]}")

    return


# 2. Write a function max(L) which examines the argument list L, and returns the largest object of type float.
#  If there is no float object in the list, then the function returns None. For example,
# max([100, 'blue', 3.5, 'sugar on the rocks', 7.0]) would return 7.0, and
# max([7, 2, 9, 1]) would return None.
# Note that type(element) == float is a way to check if element is a float.


def float_max(l):
    i_max = float("-inf")

    for i in l:
        if type(i) == float and i > i_max:
            i_max = i

    # If the max hasnt changed
    if i_max == float("-inf"):
        return None

    return i_max


def question_2():
    print(float_max([100, "blue", 3.5, "sugar on the rocks", 7.0]))
    print(float_max([7, 2, 9, 1]))


# 3. Write a function longest(L) which examines the argument list L and returns the longest string.
# You can assume all of the elements of the list L are strings, and that the list is not empty.
# Use the approach where there is a variable largestyet which is initialized to the first element of L.
# Then go through the rest of the elements and update largestyet whenever you encounter a longer string.
# For example, longest(['blue', 'red', 'the old barn', 'the white house', 'green']) would return 'the white house'.


def longest(l):
    longestYet = l[0]

    for i in l:
        if len(i) > len(longestYet):
            longestYet = i

    return longestYet


def question_3():
    print(longest(["blue", "red", "the old barn", "the white house", "green"]))


# 4. Write a program that makes both a list L and a tuple T with the following values: a) the numbers 1 to 100, inclusive.
# b) the odd numbers from 1 to 101, inclusive.
# c) the squares of numbers from 0 to 49, inclusive
# d) 60 random integers from 0 to 49, where you import random and use random.randrange(0, 50) to give each value.
# e) 50 zeroes, i.e., [0, 0, ...., 0] and (0, 0, ..., 0). Note, you can use repetition, as you would for a string.
# Do not use list comprehension for this question.
# Print each list and tuple using print(L) and print(T).

import random


def list_app():

    # (a)  Numbers 1-101
    num = []

    for i in range(1, 101):
        num.append(i)

    print("(a):", num)

    # (b) Odd Numbers
    odd = []

    for i in range(1, 101 + 1, 2):
        odd.append(i)

    print("\n(b):", odd)

    # (c) squares of numbers from 0 to 49
    sqrs = []

    for i in range(50):
        sqrs.append(i ** 2)

    print("\n(c):", sqrs)

    # (d) squares of numbers from 0 to 49
    rand = []

    for i in range(60):
        rand.append(random.randrange(0, 50))

    print("\n(d): ", rand)

    # (e) 50 zeros

    zeros = [0] * 50
    print("\n(e): ", zeros)


def tuple_app():

    # (a)  Numbers 1-101
    num = ()

    for i in range(1, 101):
        num = num + (i,)

    print("(a): ", num)

    # (b) Odd Numbers
    odd = ()

    for i in range(1, 101 + 1, 2):
        odd = odd + (i,)

    print("\n(b):", odd)

    # (c) squares of numbers from 0 to 49
    sqrs = ()

    for i in range(50):
        sqrs = sqrs + (i ** 2,)

    print("\n(c):", sqrs)

    # (d) random 50 int
    rand = []

    for i in range(60):
        rand += (random.randrange(0, 50),)

    print("\n(d): ", rand)

    # (e) 50 zeros

    zeros = (0,) * 50
    print("\n(e): ", zeros)


def question_4():
    print("---- List Implementation ----\n")
    list_app()
    print("\n---- Tuple Implementation ----\n")
    tuple_app()


# 5. Repeat Question 4, but this time use list comprehension, and you can skip the tuple part.
def question_5():

    # a: 1 to 100
    num = [x for x in range(1, 101)]
    print("a: ", num)

    # b: odd numbers
    odd = [x for x in range(1, 102, 2)]
    print("\n(b):", odd)

    # c: squares of the numbers from 0 to 49:
    sqr = [x ** 2 for x in range(50)]
    print("\n(c):", sqr)

    # d: 60 random int
    rand = [random.randrange(0, 50) for x in range(60)]
    print("\n(d):", rand)

    # e: 50 zeros
    zeros = [0 for x in range(50)]
    print("\n(e):", zeros)


# 6. Write a function perimeter(poly) which
# finds the perimeter of a polygon, where the input argument poly is a list of tuples, each tuple being the (x, y)
#  coordinates of a point on the polygon. The perimeter is the sum of the distances from one point to the next,
# including the distance from the last point to the first.
# The distance between (x1, y1) and (x2, y2) is
# sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
# Try your function on a square, a rectangle, and a triangle, where you know what the answer should be.
# Note: to use sqrt, import math, and refer to sqrt as math.sqrt.

import math

# v1 and v2 are vertices
def distance(v1, v2):
    return math.sqrt((v2[0] - v1[0]) ** 2 + (v2[1] - v1[1]) ** 2)


#! The function only produce accurate result if the each index's adjacent indexes represents vertice's edges.
#! Ex. [(1,1)(1,2)(2,2)] so for point 1,1 --> 1,2 and 2,2 are its connecting edges makes a triangle.
def perimeter(poly):
    # Base condition
    if len(poly) == 1:
        return "Unable to calculate perimeter"

    acc = 0

    for i in range(len(poly)):
        acc += distance(poly[i - 1], poly[i])

    return acc


def question_6():
    print("Square: ", perimeter([(1, 1), (1, 2), (2, 2), (2, 1)]))
    print("Rectangle: ", perimeter([(1, 1), (1, 2), (4, 2), (4, 1)]))
    print("Triange: ", perimeter([(1, 2), (2, 4), (4, 2)]))


# ---------------------------------------------------------------q7.py
# Write a function permutation(L) which
# returns a random permutation of L by the following method:
# (0) initialize an empty list P and a copy of L: C = list(L)
# (1) Use random.randrange(0, len(C)) to get a random index, i
# (2) remove element i from the list C using pop() and
# (3) append that element to the new list P
# (4) repeat steps (1-3) until all the elmeents are transferred from C to P # (5) return the new list P
# -------------------------------------------------------
# 1. Try your function on the sequence range(0, 30), which isn't a list,
# but it should work anyway.
# 2. Do that again to see that you get a new permuation.
# 3. Try it on [19, 4, 3, 17] two times.
# 4. Try it on poly = [(0, 0), (20, 0), (20, 10), (0, 10)] two times.
# ----------------------------------------------------------------------------
# Note: Although the random package has a function that will
# make a random permuation of a list L:
# random.sample(L, len(L))
# in this question you shouldn't use the sample() function, but
# you should try it out once so you'll remember how to use it.
# ----------------------------------------------------------------

import random


def permutation(l):
    p = []
    c = list(l)

    for i in range(len(c)):
        rand_idx = random.randrange(0, len(c))
        d_el = c.pop(rand_idx)
        p.append(d_el)

    return p


def question_7():
    print("(a) range(0,30): ", permutation(range(0, 30)))
    print("(b): two times [19,4, 2, 7]: ", permutation(permutation([19, 4, 3, 7])))
    print(
        "(c): poly [(0, 0), (20, 0), (20, 10), (0, 10)] two times: ",
        permutation(permutation([(0, 0), (20, 0), (20, 10), (0, 10)])),
    )

    # Main Block
    if __name__ == "__main__":

        questions = [
            question_1,
            question_2,
            question_3,
            question_4,
            question_5,
            question_6,
            question_7,
        ]

        # uncomment the code below to run single function
        for q in range(len(questions)):
            print(f"\n <----- Question {q+1} ------> \n")
            questions[q]()
