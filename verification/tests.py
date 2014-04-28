"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": u"https://www.google.com/ or http://lmgtfy.com/?q=keyword",
            "answer": ["https://www.google.com/","http://lmgtfy.com/?q=keyword"],
        },
        {
            "input": u'"https://192.168.0.1/", "https://127.0.0.1"',
            "answer": ["http://192.168.0.1/","https://127.0.0.1"],
        },
        {
            "input": u"http://taiwan.taipei/台灣在台北國裡?!",
            "answer": ["http://taiwan.taipei/"],
        },
    ]
}
