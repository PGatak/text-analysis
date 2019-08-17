import unittest
from base import BaseTest
from analytics.statistics_m import mean, median


class TestStatMethod(BaseTest):
    """Tests for the statistics methods functions."""

    def setUp(self):
        """Create a list for use in all test methods."""
        lst = [2, 11, 2, 6, 4]
        self.flg = mean(lst)
        self.flg1 = median(lst)

    def test_median(self):
        """Compare the value of median"""
        self.assertEqual(4, self.flg1)

    def test_mean(self):
        """Compare the value of median"""
        self.assertEqual(5, self.flg)


if __name__ == "__main__":
    unittest.main()