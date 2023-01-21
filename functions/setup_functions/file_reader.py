_FILENAME = 'text_files/sample.txt'

def get_title():
    with open(_FILENAME, "r") as lst:
        return lst.readlines()[0]

def get_puzzle_or_count(value):
    final_puzzle_arr = []

    with open(_FILENAME, "r") as lst:
        line_arr = lst.readlines()
        col_len = len(line_arr[1].strip().split(' '))
        count = 1
        # CAN STILL REFACTOR CODE FOR THE WHILE LOOP, PRONE TO INFINITE LOOPS
        while True:
            # loops to check if the char array will be the same as first line
            char_arr = line_arr[count].strip().split(' ')
            if col_len == len(char_arr):
                legit_puzzle = True
                # checks to see if every element is just a single character
                for char in char_arr:
                    if len(char) != 1:  # extra check to see if it is really part 
                        legit_puzzle = False
                if legit_puzzle:
                    final_puzzle_arr.append(char_arr)
                    count += 1
                else:
                    break
            else:
                break
        if value == 'puzzle':
            return final_puzzle_arr
        elif value == 'count':
            return count
        else:
            pass #DONT FORGET TO EDIT THIS LATER

def get_words_to_find():
    final_words_arr = []

    count = get_puzzle_or_count('count')
    with open(_FILENAME, "r") as lst:
        line_arr = lst.readlines()
        for index in range(count, len(line_arr)):
            w_arr = line_arr[index].strip().split(' ')
            if w_arr[0] != '':
                final_words_arr.extend(w_arr)
        return final_words_arr


    

            

    


# sort_puzzle()
# get_title()
# get_puzzle_or_count('puzzle')
# get_words_to_find()