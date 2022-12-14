def passwordCheck(s):
    capital = False
    digit = False
    s_char = False

    for l in s:
        if l in "ABCDEFGHIJKLMNOPQRTUVWXYZ":
            capital = True
        elif l in "1234567890":
            digit = True
        elif l in " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            s_char = True

    assert capital, "Password must contains one capital letter"
    assert digit, "Password must contains one digit"
    assert s_char, "must contains one special character"

    return "Password is eligible"


try:
    print(passwordCheck("wowee"))
except AssertionError as e:
    print(e)

try:
    print(passwordCheck("Wowee"))
except AssertionError as e:
    print(e)

try:
    print(passwordCheck("W0wee"))
except AssertionError as e:
    print(e)

try:
    print(passwordCheck("W0wee!"))
except AssertionError as e:
    print(e)
