from loaders import FileLoaderGen


class CountPunctuations:
    def __init__(self, filename):
        self.file = filename
        self.flg = FileLoaderGen(self.file)

    def count_exclamation_mark(self):
        exclamation_mark_counter = 0
        for word in self.flg:
            if word == "!" or "!" in word:
                exclamation_mark_counter += 1

        return exclamation_mark_counter

    def count_question_mark(self):
        question_mark_counter = 0
        for word in self.flg:
            if word == "?" or "?" in word:
                question_mark_counter += 1

        return question_mark_counter

    def count_comma(self):
        comma_counter = 0
        for word in self.flg:
            if word == "," or "," in word:
                comma_counter += 1

        return comma_counter


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file")
    args = parser.parse_args()
    file = args.file

    cp = CountPunctuations(file)

    print("numbers of exclamation_mark", cp.count_exclamation_mark())
    print("numbers of question_mark", cp.count_question_mark())
    print("numbers of coma", cp.count_comma())
