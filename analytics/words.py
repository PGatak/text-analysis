from loaders import FileLoaderGenCleaner
from collections import Counter
from tests.data.rejected_words import reject


def count_most_common(text):
    mc = Counter(FileLoaderGenCleaner(text)).most_common()
    long_words = [(k, v) for k, v in mc if len(k) > 2 and k not in reject]
    return long_words[0:20]


def count_words(text):
    a = 0
    flg = FileLoaderGenCleaner(text)
    for word in flg:
        a += 1
    return a


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default="")
    parser.add_argument("-m", "--min_char", type=int, default="")
    parser.add_argument("-n", "--number_of_words", type=int, default="")

    args = parser.parse_args()
    print(args)

    filename = args.file
    min_ch = args.min_char
    number_of_words = args.number_of_words

    def counting_words(filename, min_ch, number_of_words):
        mc = Counter(FileLoaderGenCleaner(filename)).most_common()
        long_words = [(k, v) for k, v in mc if len(k) >= min_ch and k not in reject]
        return long_words[0:number_of_words]

    print(counting_words(filename, min_ch, number_of_words))

    print("number of words : ", count_words(filename))
