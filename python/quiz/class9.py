"""
Class 9 - Quiz
"""


def class9_quiz():
    acc = 0
    for i in range(1, 1001):
        # Main thing below:
        if str(8) not in str(i):
            acc += i

    print(acc)
