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
            "input": u"歡迎來到天龍國:http://taiwan.taipei:5566/",
            "answer": ["http://taiwan.taipei:5566/"],
        },
        {
            "input": u"https://192.168.0.1/　https://127.0.0.1 <- there is an fullwidth space A___Aa",
            "answer": ["http://192.168.0.1/交作業"],
        },
        {
            "input": u"各位同學, 這次報告要使用的server在http://192.168.0.1/交作業 ....喔抱歉不小心打錯了, 是127.0.0.1請大家>    在午夜十二點前交出 by 助教 >///<",
            "answer": ["http://192.168.0.1/交作業"],
        },
    ]
}
