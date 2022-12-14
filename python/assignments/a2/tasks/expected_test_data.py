"""Expected Data for Testing"""

# Unique
test_unique = [
    {"answer": "Alesandro's", "question": "What was the name of the first restaurant Monica was head chef at?"},
    {
        "answer": "5 times",
        "question": "How many times did Chandler and Janice break up during the entirety of Friends?",
    },
]


# Overlapping
test_overlapping = [
    {"answer": "At the gym", "question": "Where did carol first meet susan"},
    {"answer": "2 days", "question": "How long did Ross and Emily date before they got engaged?"},
    {"answer": "3 weeks", "question": "How long did Ross and Emily date before they got engaged?"},
    {"answer": "6 weeks", "question": "How long did Ross and Emily date before they got engaged?"},
    {
        "answer": "Beef",
        "question": "Which of the following ingredients were not in Rachel's iconic Thanksgiving trifle?",
    },
    {
        "answer": "Raisins and walnuts",
        "question": "Which of the following ingredients were not in Rachel's iconic Thanksgiving trifle?",
    },
    {"answer": "seven", "question": "How many brothers did Joey Tribbiani have?"},
    {"answer": "seven", "question": "How many brothers did Joey Tribbiani have?"},
    {"answer": "seven", "question": "How many sisters did Joey Tribbiani have?"},
    {"answer": "Gloria", "question": "What is the name of Phoebe's actual birth mother?"},
    {"answer": "Pheobe", "question": "What is the name of Phoebe's actual birth mother?"},
]

# QA_Dictionary
test_qa_dict = {
    "What was the name of the first restaurant Monica was head chef at?": "Alesandro's",
    "How many times did Chandler and Janice break up during the entirety of Friends?": "5 times",
}

# Questions
test_ques = [
    "What was the name of the first restaurant Monica was head chef at?",
    "How many times did Chandler and Janice break up during the entirety of Friends?",
]

# Answers
test_ans = ["Alesandro's", "5 times"]

# Frequency
test_freq = {
    "alesandro": 1,
    "what": 1,
    "was": 2,
    "the": 3,
    "name": 1,
    "of": 2,
    "first": 1,
    "restaurant": 1,
    "monica": 1,
    "head": 1,
    "chef": 1,
    "at": 1,
    "5": 1,
    "times": 2,
    "how": 1,
    "many": 1,
    "did": 1,
    "chandler": 1,
    "and": 1,
    "janice": 1,
    "break": 1,
    "up": 1,
    "during": 1,
    "entirety": 1,
    "friends": 1,
}

# Decreasing
test_dec_freq = [
    ["the", 3],
    ["was", 2],
    ["of", 2],
    ["times", 2],
    ["alesandro", 1],
    ["what", 1],
    ["name", 1],
    ["first", 1],
    ["restaurant", 1],
    ["monica", 1],
    ["head", 1],
    ["chef", 1],
    ["at", 1],
    ["5", 1],
    ["how", 1],
    ["many", 1],
    ["did", 1],
    ["chandler", 1],
    ["and", 1],
    ["janice", 1],
    ["break", 1],
    ["up", 1],
    ["during", 1],
    ["entirety", 1],
    ["friends", 1],
]
