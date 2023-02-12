import classes.container as cont

class Puzzle:

    def __init__(self, filename):
        with open (filename, 'r') as lst:
            self.line_arr = lst.readlines()
            # number of rows to know where puzzle ends
            self.count = 0
            self.title = self.get_title()
            self.puzzle_portion = self.get_puzzle_portion()
            self.words = self.get_words_to_find()
            self.puzzle_object = self.get_puzzle_object()
            

    def get_title(self):
        return self.line_arr[0]

    
    # for printing purposes only
    def get_presentable_title(self):
        print(f'\nTHIS IS YOUR {self.title}')

    
    def get_words_to_find(self):
        final_words_arr = []

        count = self.count
        for index in range(count, len(self.line_arr)):
            w_arr = self.line_arr[index].strip().split(' ')
            if w_arr[0] != '':
                final_words_arr.extend(w_arr)
        if not final_words_arr:
            raise Exception('you do not have a list of words to find')
        return final_words_arr

    
    # for printing purposes only
    def get_presentable_words(self):
        print(f'YOUR WORDS TO FIND:\n')
        for word in self.words:
            print(word)


    def get_puzzle_portion(self):
        final_puzzle_arr = []
        col_len = len(self.line_arr[1].strip().split(' '))
        count = 1
        while True:
            # loops to check if the char array will be the same as first line
            char_arr = self.line_arr[count].strip().split(' ')
            if col_len == len(char_arr):
                legit_puzzle = True
                # checks to see if every element is just a single character
                for char in char_arr:
                    if len(char) != 1:  # extra check to see if it is really part 
                        legit_puzzle = False
                if legit_puzzle:
                    final_puzzle_arr.append(char_arr)
                    count += 1
                    self.count = count
                else:
                    break
            else:
                break
        if not final_puzzle_arr:
            raise Exception('you do not have a puzzle in your file')
        else:
            return final_puzzle_arr


    # for printing purposes only
    def get_presentable_puzzle(self):
        for line in self.puzzle_portion:
            print(f"{'   '.join([item for item in line])}\n")


    # converts list of list of characters to have be their own container objects
    def get_puzzle_object(self):
        puzzle_arr = self.puzzle_portion
        puzzle_container_list = []
        for r_index, row in enumerate(puzzle_arr):
            row_container = []
            for col_index, line in enumerate(row):
                row_container.append(cont.container(line, (r_index, col_index)))
            puzzle_container_list.append(row_container)
        return puzzle_container_list

    
