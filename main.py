import functions.setup_functions.puzzle_setup as setup_f
import functions.setup_functions.file_reader as fr
import functions.search_functions.puzzle_search as search_f

if __name__ == '__main__':
    # setup_f.setup('show')
    print('\nWhat do you want to do?')
    print('\t1 - COPY CHEAT CODES TO TEXT FILE')
    print('\t2 - FIND SPECIFIC WORD IN PUZZLE')
    print('\t3 - EXIT THE PROGRAM')
    choice = input('Input your choice here:\n')
    words_arr = fr.get_words_to_find()
    for word in words_arr:
        search_f.search_single(word)
    # search_f.search_single('HRSP')