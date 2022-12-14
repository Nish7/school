# Task 3: Store the pairs from unique_QA_Pairs.txt as a dictionary

import unittest
from util import readFile as rf
from util import writeFile as wf
from expected_test_data import test_qa_dict
import json


def t3(ifp="generated_files/unique_QA_Pairs.txt", ofp="generated_files/QA Dictionary"):
    unique_pairs = rf(ifp)

    pair_dic = {}

    for i in range(0, len(unique_pairs), 2):
        q = unique_pairs[i + 1].split("question ")[1][:-1]
        a = unique_pairs[i].split("answer ")[1][:-1]
        pair_dic[q] = a

    # Store QA Dictionary
    wf(ofp, lambda f: f.write(json.dumps(pair_dic)))

    print("Task 3: QA Dictionary generated")
    return pair_dic


# --- Test Cases ---
class TestCases(unittest.TestCase):
    # len is equal to as to unique pairs
    def test_1(self):
        self.assertEqual(len(t3("tests_files/unique_QA_Pairs.test.txt", "tests_files/QA Dictionary_test").keys()), 2)

    # dict equals to be as expected
    def test_2(self):
        self.assertEqual(t3("tests_files/unique_QA_Pairs.test.txt", "tests_files/QA Dictionary_test"), test_qa_dict)


if __name__ == "__main__":
    t3()
    unittest.main(exit=True)
