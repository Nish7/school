# Task 1: How many QA pairs in QA_Pairs.txt? Here (q1, a1) is a pair, where q stands for question, and a for answer.
import unittest
from util import readFile as rf


def t1(ifp="QA_Pairs.json"):
    qa_pairs = rf(ifp)
    print(f"Task 1: Pairs Total: {len(qa_pairs)}")

    return len(qa_pairs)


# --- Test Cases ---
class TestCases(unittest.TestCase):
    # Length should be 15
    def test_1(self):
        self.assertEqual(t1("Test_Pairs.json"), 15)

    # t1 returns a type integer
    def test_2(self):
        self.assertIs(type(t1("Test_Pairs.json")), int)


if __name__ == "__main__":
    t1()
    unittest.main(exit=True)
