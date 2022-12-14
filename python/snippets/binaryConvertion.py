def binaryConvertion():
    """
    One way to convert a decimal integer to binary is to repeatedly divide the number by 2 using
    integer division, keepting track of the remainders, until the number is reduced to 0. The
    remainders written in reverse order form the binary number
    """

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
