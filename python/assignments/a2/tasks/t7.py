# Task 7: Rank the words by the decreasing order of their frequencies and output them as Decreasing_Frequency.txt. The format is the same as Frequency.txt.

from util import readFile as rf
from util import writeFile as wf
from operator import itemgetter
from expected_test_data import test_dec_freq
import unittest


def t7(ifp="generated_files/Frequency.txt", ofp="generated_files/Decreasing_Frequency.txt"):
    freq = rf(ifp)
    freq_list = [[freq[i].split(", ")[0], int(freq[i].split(", ")[1])] for i in range(len(freq))]

    dec_freq = sorted(freq_list, key=itemgetter(1), reverse=True)

    wf(ofp, lambda f: [f.write(f"{w}, {str(freq)}\n") for w, freq in dec_freq])

    print("Task 7: Decreasing_Frequency.txt generated")
    return dec_freq


# --- Test Cases ---
class TestCases(unittest.TestCase):

    # frequency are are as expected.
    def test_1(self):
        self.assertEqual(
            t7("tests_files/Frequency.test.txt", "tests_files/Decreasing_Frequency.test.txt"), test_dec_freq
        )

    # # test to check if they are decreasing
    def test_2(self):
        with open("tests_files/Decreasing_Frequency.test.txt") as f:
            dt = f.readlines()
            for i in range(len(dt) - 1):
                if int(dt[i].split(",")[1][1:-1]) < int(dt[i + 1].split(",")[1][1:-1]):
                    self.fail()


if __name__ == "__main__":
    t7()
    unittest.main(exit=True)
