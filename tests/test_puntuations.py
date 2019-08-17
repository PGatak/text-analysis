import unittest
from base import BaseTest
from analytics.punctuations import CountPunctuations


class TestCountPunctuations(BaseTest):
    """Tests for the class CountPunctuations."""

    def setUp(self):
        """Create a list for use in all test methods."""
        file_name = self.get_file_path("punctuations_test.txt")
        self.flg = CountPunctuations(file_name)

    def test_count_exclamation_mark(self):
        """Confirm exclemation marks values"""
        self.assertEqual(5, self.flg.count_exclamation_mark())

    def test_count_question_mark(self):
        """Confirm question marks values"""
        self.assertEqual(5, self.flg.count_question_mark())

    def test_count_comma(self):
        """Confirm comma values"""
        self.assertEqual(5, self.flg.count_comma())

if __name__ == "__main__":
    unittest.main()
