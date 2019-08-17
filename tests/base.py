import unittest
import os


TEST_DATA_DIR = "tests/data"


class BaseTest(unittest.TestCase):
    def get_file_path(self, name):
        return os.path.abspath(os.path.join(TEST_DATA_DIR, name))
