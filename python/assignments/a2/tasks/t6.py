# Task 6: Find the term frequency of each word (that is, the count of each word) in unique_QA_Pairs.txt, and output the frequencies as Frequency.txt. Format sample is given as Frequency.txt.

import unittest
from expected_test_data import test_freq
from util import readFile as rf
from util import writeFile as wf
from util import sanitizeWord as sw


def t6(ifp="generated_files/unique_QA_Pairs.txt", ofp="generated_files/Frequency.txt"):
    unique_pairs = rf(ifp)
    freq = {}

    for i in range(0, len(unique_pairs), 2):
        ans = unique_pairs[i].split("answer ")[1].replace("\n", "").lower()
        que = unique_pairs[i + 1].split("question ")[1].replace("\n", "").lower()

        for a in ans.split(" "):
            a = sw(a)
            if a in freq.keys():
                freq[a] += 1
            else:
                freq[a] = 1

        for q in que.split(" "):
            q = sw(q)
            if q in freq.keys():
                freq[q] += 1
            else:
                freq[q] = 1

    wf(ofp, lambda f: [f.write(f"{w}, {str(freq)}\n") for w, freq in freq.items()])

    print("Task 6: Frequency.txt generated")
    return freq


# --- Test Cases ---
class TestCases(unittest.TestCase):

    # frequencies are as expected
    def test_1(self):
        self.assertEqual(t6("tests_files/unique_QA_Pairs.test.txt", "tests_files/Frequency.test.txt"), test_freq)

    # format check: string and int seperated by comma or else fail
    def test2(self):
        t6("tests_files/unique_QA_Pairs.test.txt", "tests_files/Frequency.test.txt")
        with open("tests_files/Frequency.test.txt") as f:
            dt = f.readlines()
            for l in dt:
                l_sp = l.split(",")
                if type(l_sp[0]) != str or not l_sp[1][1:-1].isnumeric():
                    self.fail()


if __name__ == "__main__":
    t6()
    unittest.main(exit=True)
