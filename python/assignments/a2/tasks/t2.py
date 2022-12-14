# Task 2: Are these pairs unique? For example: (q1, a1) (q1, a1) are identical and overlapping; (q1, a1) (q1, a2) are overlapping, and (q1, a1) (q2, a1) are overlapping as well. If not unique, find the overlapping pairs, and generate a unique_QA_Pairs.txt file and an Overlapping.txt file. The format of unique_QA_Pairs.txt and Overlapping.txt are the same as QA_Pairs.txt.

# For (q1, a1) (q1, a1), keep (q1, a1) once; put (q1, a1) in Overlapping.txt.
# For (q1, a1) (q1, a2) and (q1, a1) (q2, a1) , keep (q1, a1) (i.e., the first occurrence of a pair with q1) and delete the others; put (q1, a1), (q1, a2) and (q2, a1) in Overlapping.txt.

import unittest
from expected_test_data import test_unique
from expected_test_data import test_overlapping

from util import readFile as rf
from util import writeFile as wf


def t2(
    ifp="QA_Pairs.json", over_ofp="generated_files/Overlapping.txt", unique_ofp="generated_files/unique_QA_Pairs.txt"
):

    qa_pairs = rf(ifp)

    qa_over = []
    qa_unique = []

    i = 0
    while i < len(qa_pairs):
        q, a = qa_pairs[i]["question"], qa_pairs[i]["answer"]
        isOverlapping = False
        isIdentical = False

        y = i + 1
        while y < len(qa_pairs):
            c_q, c_a = qa_pairs[y]["question"], qa_pairs[y]["answer"]

            if q == c_q or a == c_a:
                isOverlapping = True

                if q == c_q and a == c_a:
                    isIdentical = True
                else:
                    qa_over.append(qa_pairs[y])

                qa_pairs.pop(y)
                y -= 1

            y += 1

        if isOverlapping or isIdentical:
            qa_over.append(qa_pairs[i])
        else:
            qa_unique.append(qa_pairs[i])

        i += 1

    # Writing Files
    def qaFiles(f, data):
        for i in data:
            f.write(f'answer {i["answer"]}\nquestion {i["question"]}\n')

    wf(over_ofp, lambda f: qaFiles(f, qa_over))
    wf(unique_ofp, lambda f: qaFiles(f, qa_unique))
    print(f"Task 2 Complete: Overlapping.txt({len(qa_over)}) and unique_QA_Pairs.txt generated({len(qa_unique)})")

    return (qa_unique, qa_over)


# --- Test Cases ---
class TestCases(unittest.TestCase):
    # unique pairs equals to be as expected
    def test_1(self):
        self.assertEqual(
            t2("Test_Pairs.json", "tests_files/Overlapping.test.txt", "tests_files/unique_QA_Pairs.test.txt")[0],
            test_unique,
        )

    # overlapping pairs equals to be as expected
    def test_2(self):
        self.assertEqual(
            t2("Test_Pairs.json", "tests_files/Overlapping.test.txt", "tests_files/unique_QA_Pairs.test.txt")[1],
            test_overlapping,
        )


if __name__ == "__main__":
    t2()
    unittest.main(exit=True)
