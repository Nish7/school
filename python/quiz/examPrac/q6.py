#!/usr/bin/python3
import unittest

# --------------------------------------------------------------e133
# REVIEW: condition, loop, approximation, string, list, DICT,
# recursion, 2D, exception, class
# --------------------------------------------------------------
def q6(sentence):
    """
    Assumes sentence is a string.
    Returns a list of the most frequent words in the sentence,
    where words are obtained by sentence.split(),
    and each word is trimmed by removing trailing punctuation marks,
    where punctuation marks are any of the following letters: ';:.,!?'.

    Requirement: you must use a DICTIONARY to count frequency.

    For example,
    q6('Hey diddle diddle the cat and the fiddle, the cow jumped over the moon')
    should return ['the'] since 'the' is the most frequent word.
    q6('red; blue!! blue red']
    should return ['red', 'blue'], where the items are in any order.
    """

    dic = {}
    words_s = sentence.split(" ")
    n_words = []

    for w in words_s:
        for s in ";:.,!?":
            w = w.replace(s, "")

        n_words.append(w)

    for n in n_words:
        if n in dic.keys():
            dic[n] += 1
        else:
            dic[n] = 1

    max_val = max(dic.values())

    res = []

    for k in dic:
        if dic[k] == max_val:
            res.append(k)

    return res


# --------------------------------------------------------------
# TEST CASES
# --------------------------------------------------------------
class myTests(unittest.TestCase):
    def test1(self):
        s = "Hey diddle diddle the cat and the fiddle, the cow jumped over the moon"
        r = ["the"]
        self.assertEqual(sorted(q6(s)), r)

    def test2(self):
        s = "red, blue;, red! blue!!"
        r = ["blue", "red"]
        self.assertEqual(sorted(q6(s)), r)

    def test3(self):
        s = "Red, blUe;, red! blue!!"
        r = ["Red", "blUe", "blue", "red"]
        self.assertEqual(sorted(q6(s)), r)


if __name__ == "__main__":
    unittest.main(exit=True)
# --------------------------------------------------------------
# The End
# --------------------------------------------------------------
