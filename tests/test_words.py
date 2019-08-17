import unittest
from base import BaseTest
from analytics.words import count_most_common, count_words


class TestMostCommonCounter(BaseTest):
    """Test for the function count_most_common"""

    def setUp(self):
        """Create a list for use in all test methods."""
        file_name = self.get_file_path("loader_gen_cleaner_and_words_test.txt")
        self.flg = count_most_common(file_name)
        self.flg1 = count_words(file_name)

    def test_item_in_most_common_list(self):
        """Check the value of the item."""
        self.assertListEqual([('test', 8), ('aaaaaa', 1)], self.flg)

    def test_number_of_all_words(self):
        """Compare the value of all words"""
        self.assertTrue(10 == self.flg1)

if __name__ == "__main__":
    unittest.main()
