"""
@Title: Lab 4 
@Author - Nishil K. - 501080772 - Section 01
@Deadline - 17th Oct 
@Link - [Lab4](https://courses.ryerson.ca/d2l/lms/dropbox/user/folder_submit_files.d2l?db=218164&grpid=0&isprv=0&bp=0&ou=511519)
@Note: 'This is file can be converted into .py'
"""


# 1. In class and in the text we have discussed a program that finds the integer cube root, if it exists,
# program to find the integer fourth root, if it exists, of an integer.
# of an integer, using exhaustive enumeration. You can use that program as a model, and write a


def question_1():

    n = int(input("Enter a number:"))

    for i in range(0, n):
        if i ** 4 == n:
            return i

    return "Integer root not found"


# 2. A "finger exercise" from the text: Write a program that asks the user to enter an integer and
# prints two integers, root and power, such that 1 < power < 6 and root ** power is equal to the
# integer entered by the user. If no such pair of integers exists, it should print a message to that
# effect. Write the program so that if the user gives integer 64, then your program will answer
# that 8 ** 2 is 64, that is, it looks for the lowest power for which root ** power is the desired
# integer.


def question_2():

    n = int(input("Enter the number:"))

    for i in range(2, 6):
        for y in range(n):
            if y ** i == n:
                return f"{y} ** {i}"

    return "root and power not found!"


# 3. As in Question 2 above: Write a program that asks the user to enter an integer and prints two
# integers, root and power, such that 1 < power < 6 and root ** power is equal to the integer
# entered by the user. If no such pair of integers exists, it should print a message to that effect.
# Write the program so that if the user gives integer 64, then your program will answer that 4 ** 3
# is 64, that is, it looks for the lowest root for which root ** power is the desired integer.


def question_3():

    n = int(input("Enter the number:"))

    for i in range(n):
        for y in range(2, 6):
            if i ** y == n:
                return f"{i} ** {y}"

    return "Answer Not found!"


# 4. Read an integer N from the user, and read a phrase from the user. Print the phrase N times, each
# time on a different line.


def question_4():

    n = int(input("Input int:"))
    p = input("input a phrase:")

    for i in range(n):
        print(p)

    return ""


# 5. Ask the user to input 10 integers, and then the program prints the largest odd number that was
# entered. For example of the integers were: 10, 9, 7, 12, 2, 5, 15, 100, 90, 60, then the program
# would print 15 as the largest odd number. If there is no odd number, then the program should
# print a message to that effect.


def question_5():

    max = 0

    for i in range(10):
        n = int(input("Enter a num:"))

        if n % 2 == 1 and n > max:
            max = n

    if max == 0:
        return "No odd number"

    return max


# 6. Write a program which reads a string containing any characters from the user and prints the sum
# of the digits in the string. For example, if the string from the user is "I want 3 oranges and 24
# bananas, 1abc.", then the output would be 10, since 3 + 2 + 4 + 1 = 10. Note that a character is
# a digit if it is greater than or equal to '0' and less than or equal to '9'.


def question_6():

    n = input("Enter a phrase: ")
    acc = 0

    for i in n:
        if i in "0123456789":
            acc += int(i)

    return acc


# 7. Similar to Q6, from the text, read a string from the user which is a sequence of decimal numbers
# separated by commas, e.g., "1.23,2.4,3.123". Print the sum of the numbers, which for this
# example is the sum of 1.23 + 2.4 + 3.123 = 6.753.


def question_7():

    n = input("Enter a phrase:")
    n_split = n.split(",")

    # return sum(float(x) for x in n_split)

    acc = 0
    for i in n_split:
        acc += float(i)

    return acc


# 8. In the text and in class you saw a program for using bisection search to find the square root of x.
# Change the program so that the value of x is read from the user. Ask the user for a positive
# number. If the user gives a negative number, then ask again, repeatedly, until a positive number
# is given. Finally, use bisection search to find an approximation to the square root of x.


def question_8():

    n = int(input("Input a positive number:"))

    while n <= 0:
        n = int(input("Input a positive number:"))

    max = n
    min = 0
    epsilon = 0.0001

    while True:
        mid = (max + min) / 2
        sqr = mid ** 2

        if abs(n - sqr) <= epsilon:
            return round(mid, 5)
        elif sqr > n:
            max = mid
        elif sqr < n:
            min = mid


# 9. Write a program that uses bisection search to find the cube root of a number, where the number
# can be negative or positive.


def question_9():

    n = int(input("Input a number:"))

    abs_n = abs(n)
    max = abs_n
    min = 0
    epsilon = 0.0001
    ans = ""

    while True:
        mid = (max + min) / 2
        cb = mid ** 3

        if abs(abs_n - cb) <= epsilon:
            ans = round(mid, 5)
            break
        elif cb > abs_n:
            max = mid
        elif cb < abs_n:
            min = mid

    if n < 0:
        return float("-" + str(ans))
    else:
        return float(ans)


# 10. One way to convert a decimal integer to binary is to repeatedly divide the number by 2 using
# integer division, keepting track of the remainders, until the number is reduced to 0. The
# remainders written in reverse order form the binary number


def question_10():
    n = int(input("Enter a decimal(base 10):"))
    res = ""

    rem = n
    while rem != 1:
        if rem % 2 == 0:
            res = res + "0"
        else:
            res = res + "1"

        rem = rem // 2

    return "1" + res[::-1]


# Main Function

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
