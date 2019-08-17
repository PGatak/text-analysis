import unittest
from base import BaseTest
from analytics.sentences import SentencesStatistics


class TestSentencesStatistics(BaseTest):
    """Tests for the class SentencesStatistics."""

    def setUp(self):
        """Create a list for use in all test methods."""
        file_name = self.get_file_path("sentences_test.txt")
        self.flg = SentencesStatistics(file_name)

    def test_generate_list_of_word_lengths(self):
        """Compare words from a file with a list generated."""
        self.assertListEqual([5, 9, 9, 5, 5, 6, 6, 8, 9, 9, 5, 5, 9], self.flg.list_of_word_lengths())

    def test_number_of_sentences(self):
        """Compare the value of mean."""
        self.assertEqual(13, self.flg.number_of_sentences())

    def test_mean_sentence(self):
        """Compare the value of mean."""
        self.assertEqual(7, self.flg.mean_sentence())

    def test_median_sentence(self):
        """Compare the value of median."""
        self.assertEqual(6.0, self.flg.median_sentence())

    def test_min_sentence(self):
        """Compare the value of min."""
        self.assertEqual(5, self.flg.min_sentence())

    def test_max_sentence(self):
        """Compare the value of max."""
        self.assertEqual(9, self.flg.max_sentence())


if __name__ == "__main__":
    unittest.main()
