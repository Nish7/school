## NOT TAKEN

"""
@Title: Assignment 1
@Author - Nishil K. - 501080772 - Section 01
@Deadline - 19th Oct 
"""

# Problem: A simple, minimal and relatively effective approach for encrypting only lowercased alphabetical letters . Famous solutions include Caesar cipher approach but can be easily exploited using frequency analysis and SHA or RSA are relatively excessive encryption techniques for this given problem. A middleground encryption technique which is simple yet unpredictable. Obvious

# Solution: A relatively unknown encryption technique known as 'multiplicative cipher' seemed a good choice for the problem. This cipher technique has relatively unpredicatable alphabet mapping because unlike caesar cipher  it can not be easily recognized by frequency analysis as it does not preserve the consistent pattern with different the keys. However if given that attacker knows 'multiplicative cipher' approach has been taken it can be easily exploited using a brute force approach. Despite the vulnerability, until and unless approach/algorithm is obscured away in a software program, it shouldnt be a major issue.

# Example:
#  encode("cps", 6015)  -->  "17ivu"
#   decode("17ivy", 6015)  -->  "cps"
# So we should get 'cps' as the output

# Utility convert function
def convertTo(i, convertTo):
    if convertTo == "number":
        # ord builtin function returns int corresponding to its input char. It is subtracted with int of 'a' to produce corresponsing integers starting from 0....25.
        return ord(i) - ord("a")

    elif convertTo == "alpha":
        # chr (built-in) function return char corresponding to its input int.
        return chr(ord("a") + i)

    else:
        return "Wrong Input"


# Encoding Approach: input a string, plaintext composed of lowercase letters from "a" to "z", and a positive integer key, we know there is a correspondence between abcde...uvwxyzand 0, 1, 2 ..., 23, 24, 25 : 0 <-> a, 1 <-> b ... if c is a character of plaintext whose corresponding number is c_num, apply to c_num the function f: c_num -> f(c_num) = num * c_num % 26, then find ch the corresponding character of f(x). Note that num is related to input key and which is num = (2 * (key - 1) + 1) % 26 which produces its correponding 26's coprime number using the key. generated num is also appended in cipher which is later used for verification in decoding proccess.


def encode(plaintext, key):
    cipher = ""
    # Lowercase the plaintext to avoid capitalised input.
    plaintext = plaintext.lower()

    # check if the input is alphabet only, .isalpha is builin str method
    if not plaintext.isalpha():
        return "Invalid Input: Should only contain alphabets"

    # num is the 26's coprime and the key is rather used as an sequential index of coprimes.
    num = (2 * (int(key) - 1) + 3) % 26

    # Loop every letter of the plaintext and first convert the letter l, to corresponding number and use multiplicative modulus function to produce cipher number which is then converted to its respective alphabet.
    for c in plaintext:
        c_num = num * convertTo(c, "number") % 26
        # Concatenating its results for every letter.
        cipher += convertTo(c_num, "alpha")

    return str(num) + cipher


def decode(cipher, key):
    decoded_result = ""
    cipher_msg = ""
    cipher_num = ""

    # Lowercase the cipher to avoid capitilised input
    cipher = cipher.lower()

    # Flag to check if cipher_msg only contains alphabets and split is done.
    cipher_split = False

    # Loop through each char in input cipher to split the appended cipher_num and cipher_msg from the input cipher. Example: '139xtz' --> '139' and 'xtz'
    for x in cipher:
        if x.isnumeric():
            # Checks if all number cipher_num has been extracted and if another number is found after the split, it breaks and returns invalid input as message contains a numeric char.
            if cipher_split:
                return "Invalid Input"
            cipher_num += x
        elif x.isalpha():
            cipher_msg += x
            cipher_split = True
        else:
            "Invalid input"

    # Verify that given key matches with the cipher_num, as it should result in same value as used in encoding procces.
    if not cipher_num:
        return "Invalid cipher"
    elif int(cipher_num) != (2 * (key - 1) + 3) % 26:
        return "Wrong Key"

    # Loop through each letter in the cipher. Convert each letter to its corresponsing number and then try to check for each value of the corresponsing number of the alphabet using the function and key that it matches .
    for letter in cipher_msg:

        l_num = convertTo(letter, "number")
        c_let = None

        # Brute Force Approach : loop through each number of the alphabet and check if the alphabet mapping matches using the key. then convert the matched number, c_let to its corresponsing alphabet
        for i in range(25):
            if l_num == int(cipher_num) * i % 26:
                c_let = i
                break

        # If no matches was found, or wrong key was supplied , return 'Impossible to decode' .
        if c_let == None:
            return "Impossible to decode"

        decoded_result += convertTo(c_let, "alpha")

    return decoded_result


# Test Cases
if __name__ == "__main__":
    print("Test Case #1: Pass \n ---------------")
    print(encode("cps", 6015), "\n")

    print("Test Case #2: Pass \n --------------- ")
    print(decode(encode("cps", 6015), 6015), "\n")

    print("Test Case #3: Wrong key \n ---------------")
    print(decode(encode("cps", 6015), 26), "\n")

    print("Test Case #4: Erroneous Test (wrong cipher) \n --------------- ")
    print(decode("wqs", 12), "\n")

    print("Test Case #5: Erroneous Test (invalid input - numeric in the plaintext) \n --------------- ")
    print(encode("nk212", 1313), "\n")

    # Manual Testing
    i = input("Manual Testing: input encode/decode; 0 to quit: ")
    while i != "0":
        if i == "encode":
            msg = input("Input plaintext:")
            key = int(input("Input key:"))
            print(encode(msg, key), "\n")
        elif i == "decode":
            msg = input("Input cipher:")
            key = int(input("Input key:"))
            print(decode(msg, key), "\n")

        i = input("Manual Testing: input encode/decode; 0 to quit: ")
