# Lab 3 - Nishil K. - Python:3.9.7
# Note: I have used functions to keep the variables locally scoped for easier testing. (as recommended by our TA).
# --> Main function on line 296.

# 1) Write a program that reads a number and prints whether it is negative, zero or positive.


def question_1():
    n = float(input("Enter a number:"))

    if n == 0:
        return "Its Zero"
    elif n < 0:
        return "Negative"
    else:
        return "Positive"


# 2) Write a program that reads a floating point number and prints "zero" if the number is zero. Otherwise, it prints "positive" or "negative" (as appropriate). Add "small" if the absolute value is less than 1, and add "large" if the absolute value is greater than 1000.


def question_2():
    n = float(input("Enter a number:"))
    n_abs = abs(n)

    if n == 0:
        return "zero"
    elif n > 0:
        if n_abs < 1:
            return "small, positive"
        elif n_abs > 1000:
            return "large, positive"
        else:
            return "positive"
    else:
        if n_abs < 1:
            return "small, negative"
        elif n_abs > 1000:
            return "large, negative"
        else:
            return "negative"


# 3) Write a program that reads an integer and prints how many digits it has by checking whether the number is >= 10, >= 100, and so on. However, if the number is greater than a million, just print "lots". If the number is negative, then first multiply it by -1.


def question_3():
    n = int(input("Enter a Number:"))

    # Checking if the n is a negative, then multiplying by -1 and reassign the to n
    if n < 0:
        n = n * (-1)

    if n >= 1000000:
        return "lots"

    if n >= 10 and n < 100:
        return 2
    elif n >= 100 and n < 1000:
        return 3
    elif n >= 1000 and n < 10000:
        return 4
    elif n >= 10000 and n < 100000:
        return 5
    elif n >= 100000 and n < 1000000:
        return 6
    else:
        return 1


# 4) Write a program that reads three numbers and prints "all the same" if they are all the same, "all different" if they are all different, and "neither" otherwise.


def question_4():
    n1 = float(input("Enter n1:"))
    n2 = float(input("Enter n2:"))
    n3 = float(input("Enter n3:"))

    if n1 == n2 == n3:
        return "All are same"
    elif (n1 != n2) and (n2 != n3) and (n1 != n3):
        return "All are different"
    else:
        return "Neither"


# 5) Write a program that reads three numbers and prints "increasing" if they are in increasing order, "decreasing" if they are in decreasing order, and "neither" otherwise. Here, "increasing" means "strictly increasing", where each value is less than the next. The sequence 3 4 4 would not be considered increasing, for example.


def question_5():
    n1 = float(input("Enter n1:"))
    n2 = float(input("Enter n2:"))
    n3 = float(input("Enter n3:"))

    if n1 > n2 and n2 > n3:
        return "decreasing"
    elif n1 < n2 and n2 < n3:
        return "increasing"
    else:
        return "neither"


# 6) Repeat Exercise 5, but first ask the user whether "increasing/decreasing" should be "strict" or "lenient". In lenient mode, the sequence 3 4 4 is "increasing", and the sequence 4 4 4 is both increasing and decreasing.


def question_6():
    n1 = float(input("Enter n1:"))
    n2 = float(input("Enter n2:"))
    n3 = float(input("Enter n3:"))
    mode = input("Enter Mode:")

    # Strict Mode
    if mode == "strict":
        # return strict_sequence(n1, n2, n3)
        if n1 > n2 and n2 > n3:
            return "decreasing"
        elif n1 < n2 and n2 < n3:
            return "increasing"
        else:
            return "neither"
    # Lenient Mode
    elif mode == "lenient":
        if n1 >= n2 and n2 >= n3:
            return "decreasing"
        elif n1 <= n2 and n2 <= n3:
            return "increasing"
    else:
        return "invalid mode"


# 7) Write a program that reads in three integers and prints "in order" if they are sorted in order either ascending or descending, or "not in order" otherwise. For example, 1 2 3 is "in order", 1 5 2 is "not in order", 5 2 1 is "in order", and 1 2 2 is "in order".


def question_7():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    n3 = int(input("Enter n3:"))

    if (n1 >= n2 and n2 >= n3) or (n1 <= n2 and n2 <= n3):
        return "in order"
    else:
        return "not in order"


# 8) Write a program that reads four integers and prints "two pairs" if the input consists of two matching pairs (in some order) and "not two pairs" otherwise. For example, 1 2 2 1 is "two pairs", 1 2 2 3 is "not two pairs", and 2 2 2 2 is "two pairs".


def question_8():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))
    n3 = int(input("Enter n3:"))
    n4 = int(input("Enter n4:"))

    # Approach: iterative; without making a dict.
    n_list = [n1, n2, n3, n4]

    matches = 0
    for i in range(len(n_list) - 1):
        for y in range(i + 1, len(n_list)):
            if n_list[i] == n_list[y]:
                matches += 1

    if matches == 6 or matches == 2:
        return "two pairs"
    else:
        return "not two pairs"


# 9) Write a program that reads a temperature value and the letter C for Celsius or F for Fahrenheit. Print whether water is liquid, solid, or gaseous at the given temperature at sea level.


def question_9():

    temp = float(input("Enter a temp"))
    unit = input("Enter a unit")

    if unit != "C" and unit != "F":
        return "Invalid Unit"

    if (unit == "C" and temp <= 0) or (unit == "F" and temp <= 32):
        return "Solid"
    elif (unit == "C" and temp >= 100) or (unit == "F" and temp >= 212):
        return "Gaseous"
    else:
        return "Liquid"


# 10) Write a program that translates a letter grade into a number grade. Letter grades are A, B, C, D, and F, possibly followed by + or -. Their numeric values are 4, 3, 2, 1, and 0. There is no F+ or F-. The symbol + increases the numeric value by 0.3, and the symbol - decreases it by 0.3. For example:
# Enter a letter grade: B-
# The numeric value of B- is 2.7.


def question_10():
    g = input("Enter the grade:")

    # Approach: Branching; without a dict.
    letter = g[0]
    g_sign = g[-1]

    sign = 0

    if g_sign == "+":
        sign = 0.3
    else:
        sign = -0.3

    if letter == "A":
        grade = 4
    elif letter == "B":
        grade = 3
    elif letter == "C":
        grade = 2
    elif letter == "D":
        grade = 1
    elif letter == "F":
        return 0
    else:
        return "Invalid Grade"

    return grade + sign


# 11) Write a program with a loop to computer the sum of all the even numbers from 2 to 100 inclusive.


def question_11():
    n1 = 2
    n2 = 100

    sum = 0

    for i in range(n1, n2 + 1):
        if i % 2 == 0:
            sum += i

    return sum


# 12) Write a program with a loop to compute the sum of all the squares from 1 to 100 inclusive


def question_12():
    n1 = 1
    n2 = 100

    sum = 0

    for i in range(n1, n2 + 1):
        sum += i ** 2

    return sum


# 13) Write a program with a loop to compute and print the powers of 2, for powers 0 to 20 inclusive.


def question_13():
    for i in range(0, 21):
        print(2 ** i)


# 14) Write a program with a loop to compute the sum of all the odd numbers from a to b inclusive, where a and b are inputs.


def question_14():
    n1 = int(input("Enter n1:"))
    n2 = int(input("Enter n2:"))

    sum = 0

    for i in range(n1, n2 + 1):
        if i % 2 == 1:
            sum += i

    return sum


# 15) Write a program with a loop to compute the sum of all odd digits of an input. For example, if the input is 32677, the sum would be 3 + 7 + 7 = 17.


def question_15():
    inp = input("Enter a number:")

    sum = 0

    for i in range(len(inp)):
        int_n = int(inp[i])
        if int_n % 2 == 1:
            sum += int_n

    return sum


# Main Function
if __name__ == "__main__":
    # print(question_1())
    # print(question_2())
    # print(question_3())
    # print(question_4())
    # print(question_5())
    # print(question_6())
    print(question_7())
    # print(question_8())
    # print(question_9())
    # print(question_10())
    # print(question_11())
    # print(question_12())
    # print(question_13())
    # print(question_14())
    # print(question_15())
