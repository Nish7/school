# Task 5: Generating Answers.txt

import unittest
from util import readFile as rf
from util import writeFile as wf
from expected_test_data import test_ans


def t5(ifp="generated_files/QA Dictionary", ofp="generated_files/Answers.txt"):
    qa_dict = rf(ifp, "r")
    a = list(qa_dict.values())

    wf(ofp, lambda f: [f.write(str(i + "\n")) for i in a])
    print("Task 5: Answers.txt generated")

    return a


# --- Test Cases ---
class TestCases(unittest.TestCase):
    # Questions are as expected to be
    def test_1(self):
        self.assertEqual(t5("tests_files/QA Dictionary_test", "tests_files/Answers.test.txt"), test_ans)

    # answers.test.txt have each answers on each newline
    def test_2(self):
        with open("tests_files/Answers.test.txt") as f:
            noNewline = False
            fl = f.readlines()
            for l in fl:
                if "\n" not in l:
                    noNewline = True

            if noNewline:
                self.fail()


if __name__ == "__main__":
    t5()
    unittest.main(exit=True)
