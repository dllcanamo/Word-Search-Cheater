from unittest import TestCase

import functions.setup_functions.puzzle_setup as puzzle_set
import functions.setup_functions.file_reader as fr

class SetUpFunctions(TestCase):
    def setUp(self) -> None:
        pass

    def test_non_existent_action(self):
        with self.assertRaises(Exception) as err_context:
            puzzle_set.setup('some_non_existent_action')
        self.assertEqual(str(err_context.exception), 'key passed is non existent')

    def test_get_title(self):
        title = fr.get_title()
        self.assertTrue(title, 'text file does not contain a title')

    def test_get_puzzle_puzzle(self):
        puzzle = fr.get_puzzle_or_count('puzzle')
        self.assertTrue(puzzle, 'puzzle cannot be retrieved')

    def test_get_puzzle_count(self):
        count = fr.get_puzzle_or_count('count')
        self.assertTrue(count, 'count cannot be retrieved')

    def test_get_puzzle_non_existent_value(self):
        with self.assertRaises(Exception) as err_context:
            fr.get_puzzle_or_count('some_non_existent_value')
        self.assertEqual(str(err_context.exception), 'key passed is non existent')

    def test_get_words(self):
        words = fr.get_words_to_find()
        self.assertTrue(words, 'list of words cannot be retrieved')

# class Search 

    

    

    


