import os

from classes.puzzle import Puzzle as pz
import functions.search_functions.puzzle_search as search_f

_CHEAT_CODES_FOLDER_NAME = 'cheat_codes'
_FILENAME = 'text_files/sample.txt'

def present_puzzle():
    puzzle.get_presentable_title()
    puzzle.get_presentable_puzzle()
    puzzle.get_presentable_words()

if __name__ == '__main__':
    program_should_not_exit = True

    # check if file exists
    if not os.path.isfile(_FILENAME):
        raise Exception('the file currently does not exist')
    # instantiate a new puzzle object set
    puzzle = pz(_FILENAME)
    # pass the puzzle object to file containing search algorithm
    search_f.setup_puzzle_object_for_search(puzzle)


    while program_should_not_exit:
        print('\nWELCOME TO WORD SEARCH CHEATER!')
        print('What do you want to do?')
        print('\t1 - COPY CHEAT CODES TO TEXT FILE')
        print('\t2 - FIND SPECIFIC WORD IN PUZZLE')
        print('\t3 - EXIT THE PROGRAM')
        choice = input('Input your choice here:\n')

        if choice == '1':
            os.system('cls||clear')
            os.makedirs(f'{_CHEAT_CODES_FOLDER_NAME}/', exist_ok=True)
            title = '_'.join(puzzle.get_title().split(' '))[:-1]
            filename = f'{_CHEAT_CODES_FOLDER_NAME}/{title}_cheats.txt'
            os.system('cls||clear')
            with open(filename, 'w') as f:
                for word in puzzle.words:
                    search_f.search_single(word, filename)
            print('YOUR CHEAT CODES ARE SUCCESFULLY CREATED!, YOU\'RE WELCOME!')
        elif choice == '2':
            chosen_word = None
            while not chosen_word:
                os.system('cls||clear')
                print('These is/are your word/s to find!')
                print('Select the number of the corresponding word to find its location\n')
                words_arr = puzzle.words
                for index, word in enumerate(words_arr):
                    print(f'{index + 1} - {word}')
                pos = input('Selected number: ')
                if int(pos) - 1 in range(0, len(words_arr)):
                    chosen_word = words_arr[int(pos) - 1]
                else:
                    print('Please try again, your input is not part of the available inputs')
            # print('\n')
            os.system('cls||clear')
            search_f.search_single(chosen_word)
        elif choice == '3':
            os.system('cls||clear')
            print('THANK YOU FOR USING WORD SEARCH CHEATER, BYE!')
            program_should_not_exit = False
        else:
            os.system('cls||clear')
            print('unidentified input, please try again')

