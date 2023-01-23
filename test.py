from unittest import TestCase

import functions.setup_functions.puzzle_setup as pset
import functions.setup_functions.file_reader as fr
import functions.search_functions.orientation_mainpulator as om
import functions.search_functions.puzzle_search as psearch

class SetUpFunctions(TestCase):
    def setUp(self) -> None:
        pass

    def test_non_existent_action(self):
        with self.assertRaises(Exception) as err_context:
            pset.setup('some_non_existent_action')
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

class SearchFunctions(TestCase):
    def setUp(self) -> None:
        pass

    def test_manipulate_empty_array(self):
        with self.assertRaises(Exception) as err_context:
            om.manipulate(None)
        self.assertEqual(str(err_context.exception), 'there is no array being passed')

    def test_search_single_missing_word(self):
        with self.assertRaises(Exception) as err_context:
            psearch.search_single('NONEXISTENTWORD')
        self.assertEqual(str(err_context.exception), 'you are looking for a word that is not in the list of words')

    def test_process_answer_missing_match_list(self):
        with self.assertRaises(Exception) as err_context:
            psearch.process_answer(None, None)
        self.assertEqual(str(err_context.exception), 'parameter passed is non existent')

    def test_process_answer_invalid_keys(self):
        with self.assertRaises(Exception) as err_context:
            psearch.process_answer(['SOMETHING','something',100,(100,101)],None)
        self.assertEqual(str(err_context.exception), 'key passed is non existent')

    


        

    

    

    


