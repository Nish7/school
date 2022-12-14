# Utility Function
import os

# Utility function for reading files: Used throughout the the assignments tasks
def readFile(path, isEval=False):

    with open(path, "r", encoding="utf-8-sig") as f:
        if isEval or path.split(".")[-1] == "json":
            return eval(f.read())  # eval function takea the input and eval. as a python code
        else:
            return f.readlines()


def writeFile(path, fn):

    if not os.path.exists("generated_files"):
        os.mkdir("generated_files")
    elif not os.path.exists("tests_files"):
        os.mkdir("tests_files")

    with open(path, "w", encoding="utf-8-sig") as f:
        fn(f)


# Sanatize Words: Removing puctuations and grammar
def sanitizeWord(w):
    strRemove = ["'s", "?", ",", "'", ".", "’", "‘" ";"]
    for s in strRemove:
        w = w.replace(s, "")

    return w
