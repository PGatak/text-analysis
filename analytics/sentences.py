from analytics.statistics_m import mean, median
from loaders import FileLoaderGen
import string


class SentencesStatistics:

    def __init__(self, filename):
        self.file = filename
        self.flg = FileLoaderGen(self.file)

    def list_of_word_lengths(self):

        word_count = 0
        lst = []

        for word in self.flg:
            word_count += 1
            if (not word.startswith("." + string.ascii_letters) and
                (word.endswith(".") or
                 word.endswith("?") or
                 word.endswith("!"))):
                lst.append(word_count)
                word_count = 0

        return lst

    def number_of_sentences(self):
        return len(self.list_of_word_lengths())

    def mean_sentence(self):
        return round(mean(self.list_of_word_lengths()))

    def median_sentence(self):
        return median(self.list_of_word_lengths())

    def min_sentence(self):
        return min(self.list_of_word_lengths())

    def max_sentence(self):
        return max(self.list_of_word_lengths())


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()
    file = args.file
    s = SentencesStatistics(file)
    print(s.list_of_word_lengths())
    print(s.number_of_sentences())
    print(s.mean_sentence())
    print(s.median_sentence())
    print(s.min_sentence())
    print(s.max_sentence())

