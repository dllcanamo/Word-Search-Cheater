import classes.container as cont
import functions.setup_functions.file_reader as fr

def setup(action):
    puzzle_arr = fr.get_puzzle_or_count('puzzle')
    title = fr.get_title()
    words = fr.get_words_to_find()
    puzzle_container_list = []
    for r_index, row in enumerate(puzzle_arr):
        row_container = []
        for col_index, line in enumerate(row):
            row_container.append(cont.container(line, (r_index, col_index)))
        puzzle_container_list.append(row_container)
    # displays a clean word search puzzle in terminal
    if action == 'show':
        print(f'\nTHIS IS YOUR {title}')
        for line in puzzle_container_list:
            print(f"{'   '.join([item.value for item in line])}\n")
        print(f'YOUR WORDS TO FIND:\n')
        for word in words:
            print(word)
    elif action == 'use':
        return [title, puzzle_container_list, words]



    

