"""
@Title: Lab 7
@Author - Nishil K. - 501080772 - Section 01
@Deadline - 10th Nov 
@Note: 'This file can be converted into .py'
"""

import random


# 1. A run is a sequence of adjacent repeated values. Write a program that generates a sequence of 20 random die tosses and then prints the die values, marking the runs by including them in parentheses, like this:


def diceToss(n):
    rolls = []

    for i in range(n):
        rolls.append(random.randrange(1, 6 + 1))

    return rolls


def seq():
    # rolls = diceToss(20)
    rolls = [1, 2, 2, 2, 3, 3, 3, 5, 4, 4]

    sequence = ""
    inRun = False

    for i, r in enumerate(rolls[:-1]):
        if inRun:
            if r != rolls[i - 1]:
                sequence += ")"
                inRun = False
        else:
            if r == rolls[i + 1]:
                sequence += "("
                inRun = True

        sequence += str(r)

    if inRun:
        sequence += ")"

    return sequence


def question_1():
    print(seq())


# 2. Write a program that generates a sequence of 20 random die tosses and that prints the die values, marking only the longest run, like this:
# 1 2 5 5 3 3 2 4 3 (2 2 2 2) 3 6 5 5 6 3 1


def largestSeq():
    rolls = diceToss(20)
    print(rolls)

    largestSeq = 0
    l_idx = None

    for i, r in enumerate(rolls[:-1]):
        l_seq = 0

        y = i + 1
        while y < len(rolls) and r == rolls[y]:
            l_seq += 1
            y += 1

        if l_seq > largestSeq:
            largestSeq = l_seq
            l_idx = i

    if l_idx == None or largestSeq == 0:
        return "".join([str(a) for a in rolls])

    rolls.insert(l_idx, "(")
    rolls.insert(l_idx + largestSeq + 2, ")")

    return "".join([str(a) for a in rolls])


def question_2():
    print(largestSeq())


# 3. Assume that L is a list of Boolean values, True and False. Write a function longestFalse(L) which returns a tuple (start, end) representing the start and end indices of the longest run of False values in L. If there is a tie, then return the first such run. For example, if L is
# False False True False False False False True True False False 0 1 2 3 4 5 6 7 8 9 10
# then the function would return (3, 6), since the longest run of False is from 3 to 6.


def longestFalse(L):
    longestF = 0
    l_idx = None

    for i, r in enumerate(L[:-1]):
        if r == False:

            l_seq = 1
            y = i + 1

            while y < len(L) and L[y] == False:
                l_seq += 1
                y += 1

            if l_seq > longestF:
                longestF = l_seq
                l_idx = i

    if l_idx == None and L[-1] == False:
        l_idx = len(L) - 1
        longestF = 1

    if l_idx == None and longestF == 0:
        return (None, None)

    return (l_idx, l_idx + longestF - 1)


def question_3():
    print(longestFalse([False, False, False, False, True, True, False, False, False, False, False]))
    print(longestFalse([True, True, True, True, False]))


# 4. Write a function occupy(n), which shows how birds are going to occupy n nests, assuming that each new bird will choose the nest in the middle of the largest unoccupied run of nests. You could use as a helper method longestFalse(L) from the previous question. For example, if there were 10 nests, occupy(10) would print out the following sequence, where underscore indicates an unoccupied nest, and X indicates an occupied nest. The first line of the printout is just 10 underscores showing that all the nests are unoccupied. The second line shows that a bird came to nest in position 5, since that is one the first middle positions of the unoccupied run from 0 to 9. In the third line a bird came to occupy the middle position for the longest open run of nests, from 0 to index 4

import math


def nestPrint(nest):
    def isOccupied(b):
        if b:
            return "X"
        else:
            return "_"

    return "".join(list(map(isOccupied, nest)))


def occupy(n):
    i_nests = [False] * n
    print(nestPrint(i_nests))

    while i_nests != ([True] * n):
        largest_range = longestFalse(i_nests)
        start, end = largest_range[0], largest_range[1]
        mid_idx = math.ceil((start + end) / 2)
        i_nests[mid_idx] = True
        print(nestPrint(i_nests))


def question_4():
    occupy(10)


# 5. Write a function isPal(L), where L is a list of integers, and the function returns True if the list is a palindrome, False otherwise. For example [5, 2, 9, 9, 2 5] is a palindrome. Use the reverse() method of list and check if the reversed list is the same as the original list.


def isPal(L):

    l_c = L[:]  # L shallow copy, so reverse does not mutate the list
    l_c.reverse()

    if L == l_c:
        return True
    else:
        return False


def question_5():
    print(isPal([5, 2, 9, 9, 2, 5]))


# Main Block
if __name__ == "__main__":

    questions = [
        question_1,
        question_2,
        question_3,
        question_4,
        question_5,
    ]

    # uncomment the code below to run single function
    for q in range(len(questions)):
        print(f"\n <----- Question {q+1} ------> \n")
        questions[q]()
