import re

import functions.setup_functions.puzzle_setup as setup_f
import functions.search_functions.orientation_mainpulator as om

def search_single(keyword):
    array = setup_f.setup('use')
    # print(array)
    if array: #to make sure it is not empty
        conts = array[1]
        words = array[2]
        manipulated_obj = om.manipulate(conts)
        for key in manipulated_obj:
            for i in manipulated_obj[key]:
                print(f'{key}, {i}, {manipulated_obj[key][i]}')
                match = re.search(keyword, manipulated_obj[key][i])
                if match:
                # if manipulated_obj[key][i] == keyword:
                    print(f'Found it!, it is at {key}, {i}')
    





