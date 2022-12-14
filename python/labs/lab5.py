"""
@Title: Lab 5
@Author - Nishil K. - 501080772 - Section 01
@Deadline - 24th Oct 
@Note: 'This is file can be converted into .py'
"""


# 1. Write a function called helloWorld(), which prints "Hello World". Next write a program that
# calls that function once. In the same program, add a loop which calls the function 10 times.


def helloWorld():
    return "Hello, World!"


def question_1():
    for i in range(10):
        print(helloWorld())

    return ""


# 2. Write a function hello(name), which prints "Hello" followed by the value of name. For
# example, hello('Ahmad') would print "Hello Ahmad". Write a program that asks the user for
# their name, and then uses the function to greet the person.


def hello(name):
    return f"Hello {name}"


def question_2():
    i = input("Enter a name: ")
    return hello(i)


# 3. Write a function hello(firstname, lastname), which, for example, if called with hello('John',
# 'Smith'), would print two lines:


def helloTwo(fname, lname):
    return f"Hello {fname} {lname}\nHello {lname}, {fname}"


def question_3():
    fn = input("Input the first name: ")
    ln = input("Input the last name: ")
    return helloTwo(fn, ln)


# 4. Write a function repeatPhrase(phrase, n), which prints the given phrase n times, alternating
# between lowercase and uppercase. Recall, that if aString is a string, then a.upper() is the
# uppercase of that string, and a.lower() is the lower case of the string. For example, repeat('The
# sky is blue', 5) would print:


def repeatPhase(phr, n):
    for i in range(n):
        if i % 2 == 0:
            print(phr.lower())
        else:
            print(phr.upper())


def question_4():
    i = input("Input the phrase: ")
    n = int(input("Input the num: "))

    repeatPhase(i, n)
    return ""


# 5. Write a function timestable(n), which prints a multiplication table of size n. For example,
# timestable(5) would print:


def row(n, m):
    col = ""
    for y in range(1, n + 1):
        col += f"{m*y:3}"

    return col


def timestable(n):
    for i in range(1, n + 1):
        print(row(n, i))


def question_5():
    n = int(input("Input the n: "))
    timestable(n)
    return ""


# 6. Write a function perfectcube(n), which returns True if n is a perfect cube and returns False
# otherwise. Notice that this function is not printing anything, but rather returning True or False.
# The function must use exhaustive enumeration to check if n is a perfect cube. That means
# checking if 0**3 is n or 1**3 is n or 2**3 is n, and so on, up to where it is pointless to check
# further. (Instead of n, you might be checking against abs(n), since for example, -125 is a perfect
# cube. Use the function in a program where you ask the user for n and you print a statement like
# "Yes, that is a perfect cube" or "No, that number is not a perfect cube", as appropriate.


def perfectcube(n):
    n = abs(int(n))

    for i in range(n):
        if i ** 3 == n:
            return True

    return False


def question_6():
    n = int(input("Enter a n: "))

    if perfectcube(n):
        print("Yes, that is a perfect cube ")
    else:
        print("No, that number is not a perfect cube")

    return ""


# 7. Write a function biggestOdd(), which reads in numbers from the user until the user enters 0.
# Then the function returns (not prints) the largest odd number that was entered. For example, if
# the integers were: 10, 9, 7, 12, 2, 5, 15, 100, 90, 60, 0, then the program would return 15 as the
# largest odd number. Similarly, if the integers were -55, -33, -10, 100, -5, 0, then the program
# would return -33 as the largest odd number. If there is no odd number, then the function should
# return 0. Use the function in a program to check that it works.


def biggestOdd():
    n = int(input("Enter a num:"))
    max = float("-inf")

    while n != 0:
        if n % 2 == 1 and n > max:
            max = n

        n = int(input("Enter a num:"))

    if max == float("-inf"):
        return 0

    return max


def question_7():
    print(biggestOdd())
    return ""


# 8. Write a function biggestBuried(s), which the parameter s is a string, and the function returns
# the largest integer buried in the string. If there is no integer inside the string, then return 0


def biggestBuried(s):
    max = 0
    temp = ""

    for i in s:
        if i.isdigit():
            temp += i
            if max < int(temp):
                max = int(temp)
        else:
            temp = ""

    return max


def question_8():
    i = input("Enter a phrase: ")
    return biggestBuried(i)


# 9. Write a function squareRoot(x, epsilon) that uses bisection search to return a number y that is
# close enough to the square root of x, so that abs(y**2 - x) < epsilon. Try out the function in a
# program to verify that it works properly


def squareRoot(x, epsilon):
    n = int(x)
    epsilon = float(epsilon)

    while n <= 0:
        n = int(input("Input a positive number:"))

    max = n
    min = 0

    while True:
        mid = (max + min) / 2
        sqr = mid ** 2

        if abs(n - sqr) <= epsilon:
            return round(mid, 5)
        elif sqr > n:
            max = mid
        elif sqr < n:
            min = mid


def question_9():
    i = input("Input num: ")
    e = input("Input epsilon: ")
    return squareRoot(i, e)


# 10. Write a function decimalToBinary(n) that converts a positive decimal integer n to a string
# representing the corresponding binary number. Do the conversion by repeatedly dividing the
# number n by 2 using integer division, keepting track of the remainders, until the number is
# reduced to 0. The remainders written in reverse order form the binary number string. The
# following table (also shown in an earlier lab) illustrates the process.


def decimalToBinary(n):
    n = int(n)
    res = ""

    if n == 0:
        return "0"

    rem = n
    while rem != 1:
        if rem % 2 == 0:
            res = res + "0"
        else:
            res = res + "1"

        rem = rem // 2

    return "1" + res[::-1]


def question_10():
    for i in range(10):
        print(f"{decimalToBinary(i)} is the binary of {i}")

    return ""


if __name__ == "__main__":

    questions = [
        question_1,
        question_2,
        question_3,
        question_4,
        question_5,
        question_6,
        question_7,
        question_8,
        question_9,
        question_10,
    ]

    # uncomment the code below to run single function
    for q in range(0, 10):
        print(f"\n <----- Question {q+1} ------> \n")
        print(questions[q]())
