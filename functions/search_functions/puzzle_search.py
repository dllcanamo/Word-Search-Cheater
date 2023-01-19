import functions.setup_functions.puzzle_setup as setup_f
import functions.search_functions.orientation_mainpulator as om

def search_single(keyword):
    array = setup_f.setup('use')
    # print(array)
    if array: #to make sure it is not empty
        conts = array[1]
        words = array[2]
        om.manipulate(conts)
    





