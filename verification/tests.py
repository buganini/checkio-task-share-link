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
            "input": u"https://www.google.com/ 或 http://lmgtfy.com/?q=keyword",
            "answer": [u"https://www.google.com/",u"http://lmgtfy.com/?q=keyword"],
        },
        {
            "input": u'https://192.168.0.1/ https://127.0.0.1',
            "answer": [u"https://192.168.0.1/",u"https://127.0.0.1"],
        },
        {
            "input": u"my test server: http://1.2.3.4:8888 not 5.5.6.6:5566",
            "answer": [u"http://1.2.3.4:8888"],
        },
        {
            "input": u"http://台灣.taipei/ ....台湾は台北国の中ですか？",
            "answer": [u"http://台灣.taipei/"],
        },
        {
            "input": u">////< http://www.pixiv.net/pic.php?tag=パズドラ",
            "answer": [u"http://www.pixiv.net/pic.php?tag=パズドラ"]
        },
        {
            "input": u"http://qwer:1234/?鍵=值　小心，有全形空白；be careful, there are full width space",
            "answer": [u"http://qwer:1234/?鍵=值"],
        }
    ]
}
