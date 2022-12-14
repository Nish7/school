"""
Title: Lab 4
@Date:4th Oct, 21
"""

# Write a function that accepts one string & one character and return how many times that character appears in the string; case sensitive too


def quiz_4(phrase, char):
    cnt = 0

    # Looping through each char in the string
    for i in phrase:
        # Comparing it with the given input char, if true then increment the cnt variable
        if i == char:
            cnt += 1

    return cnt


print(quiz_4("aaaAAAssA", "A"))
