import unittest
from base import BaseTest
from loaders import FileLoaderGen, FileLoaderGenCleaner


class TestFileLoaderGen(BaseTest):
    """Tests for the class FileLoaderGen."""

    def setUp(self):
        """Create a list for use in all test methods."""
        file_name = self.get_file_path("loader_gen_test.txt")
        self.flg = FileLoaderGen(file_name)
        self.word = [word for word in self.flg]

    def test_generate_list(self):
        """Compare words from a file with a list generated."""
        self.assertListEqual(['jeden', 'dwa', 'trzy', 'cztery',
                              'piec', 'szesc', 'siedem', 'osiem', 'dziewiec',
                              'dziesiec'],
                             self.word)

    def test_item_in_list(self):
        """Check if the item is in the list."""
        self.assertIn('jeden', self.word)

    def test_instance(self):
        """Confirm that the list has been created."""
        self.assertTrue(isinstance(self.word, list))


class TestFileLoaderGenCleaner(BaseTest):
    """Tests for the class FileLoaderGenCleaner."""

    def setUp(self):
        """Create a list for use in all test methods."""
        file_name = self.get_file_path("loader_gen_cleaner_and_words_test.txt")
        self.flg = FileLoaderGenCleaner(file_name)
        self.word = [word for word in self.flg]

    def test_generate_clean_list(self):
        """Compare words from a file with a list generated."""
        self.assertListEqual(
            ['test', 'aaaaaa', 'test', 'b', 'test', 'test', 'test',
             'test', 'test', 'test'],
            self.word)


if __name__ == "__main__":
    unittest.main()
