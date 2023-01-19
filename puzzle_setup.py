import classes.container as cont
import file_reader as fr

# _cont = cont.container(1,2)
# print(_cont.value)

puzzle_arr = fr.get_puzzle_or_count('puzzle')
for line in puzzle_arr:
    print(line)

