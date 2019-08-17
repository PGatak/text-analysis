from analytics.words import count_words, count_most_common
from analytics.sentences import SentencesStatistics
from analytics.punctuations import CountPunctuations
from tests.data.rejected_words import reject
from loaders import FileLoaderGenCleaner
import pprint


class Template:
    def __init__(self, filename):
        self.file = filename

    def file_name(self):
        return self.file

    def number_of_words(self):
        return count_words(self.file)

    def number_of_sentences(self):
        return SentencesStatistics(self.file).number_of_sentences()

    def average_sentences(self):
        return SentencesStatistics(self.file).mean_sentence()

    def median_sentences(self):
        return SentencesStatistics(self.file).median_sentence()

    def exclamation_mark(self):
        cp = CountPunctuations(self.file).count_exclamation_mark()
        mean_cp = (cp / SentencesStatistics(self.file).number_of_sentences()) * 100
        return mean_cp

    def question_mark(self):
        cp = CountPunctuations(self.file).count_question_mark()
        mean_cp = (cp / SentencesStatistics(self.file).number_of_sentences()) * 100
        return mean_cp

    def comma(self):
        cp = CountPunctuations(self.file).count_comma()
        mean_cp = (cp / SentencesStatistics(self.file).number_of_sentences()) * 100
        return mean_cp

    def longest_word(self):
        d = dict()
        for word in FileLoaderGenCleaner(self.file):
            if word not in reject:
                d[word] = len(word)
        max_l = max(d.values())

        return [word for word in d if len(word) == max_l], max_l

    def most_common_words(self):
        return pprint.pprint(count_most_common(self.file))


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")

    args = parser.parse_args()

    for filename in args.files:
        print("".center(72, "-"))
        print("File name", Template(filename).file_name())
        print("The number of all words : ", Template(filename).number_of_words())
        print("The number of all sentences : ", Template(filename).number_of_sentences())
        print("The average number of words in a sentence : ", Template(filename).average_sentences())
        print("Median number of words in a sentence : ", round(Template(filename).median_sentences()))
        print("The average number of exclamation mark per 100 sent.: ", round(Template(filename).exclamation_mark(), 2))
        print("The average number of question mark per 100 sent.: ", round(Template(filename).question_mark(), 2))
        print("The average number of coma per 100 sentences : ", round(Template(filename).comma(), 2))
        print("Longest word:", Template(filename).longest_word())
        print("20 most common words : ", Template(filename).most_common_words())

