import classes.container as cont
import file_reader as fr

# def setup_puzzle():
puzzle_arr = fr.get_puzzle_or_count('puzzle')
title = fr.get_title()
puzzle_container_list = []
for r_index, row in enumerate(puzzle_arr):
    row_container = []
    for col_index, line in enumerate(row):
        row_container.append(cont.container(line, (r_index, col_index)))
    puzzle_container_list.append(row_container)
# displays a clean word search puzzle in terminal
print(f'THIS IS YOUR {title}')
for line in puzzle_container_list:
    print(f"{'   '.join([item.value for item in line])}\n")



    

