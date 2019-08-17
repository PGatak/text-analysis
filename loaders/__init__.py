
class Source():
    """The parent class for the class that opens the files"""
    def __init__(self, file_name):
        self.file = file_name


class FileLoaderGen(Source):
    def __iter__(self):
        with open(self.file, 'r', encoding="utf-8") as f:
            for line in f:
                for word in line.split():
                    yield word


class FileLoaderGenCleaner(Source):
    def __iter__(self):
        with open(self.file, 'r', encoding="utf-8") as f:
            for line in f:
                for word in line.split():
                    # handles superscripts
                    word = "".join([c for c in word if c.isalpha()])
                    if word:
                        yield word.lower()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--loader",
                        choices=["FileLoaderGen", "FileLoaderGenCleaner"])
    parser.add_argument("files", nargs="+")

    args = parser.parse_args()

    cls_loader = None
    if args.loader == "FileLoaderGen":
        cls_loader = FileLoaderGen
    elif args.loader == "FileLoaderGenCleaner":
        cls_loader = FileLoaderGenCleaner

    assert cls_loader

    for filename in args.files:
        print("".center(72, "-"))
        print(filename)
        flg = cls_loader(filename)
        for word in flg:
            print(word)
