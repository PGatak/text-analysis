from analytics.statistics_m import mean, median
from loaders import FileLoaderGen
import string


def y(flg):
    word_count = 0
    lst = []
    a = 0

    for word in flg:
        if len(lst) == a:
            if word.islower():
                word_count = lst[-1]
                lst.pop()
                a = len(lst)
        word_count += 1
        a += 1
        if not word.startswith("." + string.ascii_letters) and (word.endswith(".")
                                                                or word.endswith("?") or word.endswith("!")):
            lst.append(word_count)
            word_count = 0
        print("word_count", word_count)
        print("lst", lst)
        print("len lst", len(lst))
        print("a", a)
        print("xxxxxxxxxx")

    return lst


# print(y(["AAA...", "aaa.", "Bbb", "bbb", "bbb.", "CCC...", "ccc."]))
