import classes.container as cont
import file_reader as fr

# def setup_puzzle():
puzzle_arr = fr.get_puzzle_or_count('puzzle')
for line in puzzle_arr:
    print(line)
puzzle_container_list = []
for r_index, row in enumerate(puzzle_arr):
    row_container = []
    for col_index, line in enumerate(row):
        row_container.append(cont.container(line, (r_index, col_index)))
    puzzle_container_list.append(row_container)
# for line in puzzle_container_list:
#     print([item.position for item in line])


    

