# Task 4: Generating Questions.txt

import unittest
from expected_test_data import test_ques
from util import readFile as rf
from util import writeFile as wf


def t4(ifp="generated_files/QA Dictionary", ofp="generated_files/Questions.txt"):
    qa_dict = rf(ifp, "r")
    q = list(qa_dict.keys())

    # Writing the File
    wf(ofp, lambda f: [f.write(str(i + "\n")) for i in q])

    print("Task 4: Question.txt generated")
    return q


# --- Test Cases ---
class TestCases(unittest.TestCase):
    # Questions are as expected to be
    def test_1(self):
        self.assertEqual(t4("tests_files/QA Dictionary_test", "tests_files/Questions.test.txt"), test_ques)

    # questions.txt have each question on each newline
    def test_2(self):
        t4("tests_files/QA Dictionary_test", "tests_files/Questions.test.txt")
        with open("tests_files/Questions.test.txt") as f:
            noNewline = False
            fl = f.readlines()
            for l in fl:
                if "\n" not in l:
                    noNewline = True

            if noNewline:
                self.fail()


if __name__ == "__main__":
    t4()
    unittest.main(exit=True)
