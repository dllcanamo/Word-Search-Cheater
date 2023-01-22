def manipulate(array):
    rows = len(array)
    cols = len(array[0])
    
    orientations = {}
    #structures all horizontal arrays and their inverted versions
    horizontal = {}
    horizontal_inverted = {}
    for index, row in enumerate(array):
        # print(f"{([item.value for item in row])}")
        horizontal.update({index : ''.join([item.value for item in row])})
        horizontal_inverted.update({index : (''.join([item.value for item in row]))[::-1]})
    orientations.update({'horizontal' : horizontal})
    orientations.update({'horizontal_inverted' : horizontal_inverted})

    #structures all vertical arrays and their inverted versions
    vertical = {}
    vertical_inverted = {}
    for i in range(cols):
        vertical_str = ''
        for row in array:
            vertical_str += row[i].value
        vertical.update({i : vertical_str})
        vertical_inverted.update({i : vertical_str[::-1]})
    orientations.update({'vertical' : vertical})
    orientations.update({'vertical_inverted' : vertical_inverted})

    #structures all diagonal arrays and their inverted versions
    # diagonals from left to right
    diagonal_f_half = {}
    diagonal_f_half_inverted = {}
    diagonal_s_half = {}
    diagonal_s_half_inverted = {}
    diagonal_f_ltf_half = {}
    diagonal_f_ltf_half_inverted = {}
    diagonal_s_ltf_half = {}
    diagonal_s_ltf_half_inverted = {}

    # first half of diagonal
    for i, item in enumerate(array[0]):
        diagonal_str = ''
        exceeds_puzzle = False
        myObj = item
        while not exceeds_puzzle:
            lower_left = myObj.get_lower_left_coordinates()
            # print(myObj.value,myObj.position, lower_left)
            diagonal_str += myObj.value
            if lower_left[0] >= rows or lower_left[1] < 0:
                # print('thats the end for me!')
                exceeds_puzzle = True
            else:
                myObj = array[lower_left[0]][lower_left[1]]
        diagonal_f_half.update({i : diagonal_str})
        diagonal_f_half_inverted.update({i : diagonal_str[::-1]})
                
    # second half of diagonal
    for i in range(1,rows):
        diagonal_str = ''
        myObj = array[i][cols-1]
        exceeds_puzzle = False
        while not exceeds_puzzle:
            lower_left = myObj.get_lower_left_coordinates()
            diagonal_str += myObj.value
            # print(myObj.value,myObj.position, lower_left)
            if lower_left[0] >= rows or lower_left[1] < 0:
                # print('thats the end for me!')
                exceeds_puzzle = True
            else:
                myObj = array[lower_left[0]][lower_left[1]]
        diagonal_s_half.update({i : diagonal_str})
        diagonal_s_half_inverted.update({i : diagonal_str[::-1]})
    # print(diagonal_f_half)
    # print(diagonal_s_half)
    # print(diagonal_f_half_inverted)
    # print(diagonal_s_half_inverted)
    orientations.update({'diagonal_f_half' : diagonal_f_half})
    orientations.update({'diagonal_f_half_inverted' : diagonal_f_half_inverted})
    orientations.update({'diagonal_s_half' : diagonal_s_half})
    orientations.update({'diagonal_s_half_inverted' : diagonal_s_half_inverted})

    # first half of diagonal going left to right
    for i, item in enumerate(array[0]):
        diagonal_str = ''
        exceeds_puzzle = False
        myObj = item
        while not exceeds_puzzle:
            lower_right = myObj.get_lower_right_coordinates()
            # print(myObj.value, myObj.position, lower_right)
            diagonal_str += myObj.value
            if lower_right[0] >= rows or lower_right[1] >= cols:
                # print('thats the end for me!')
                exceeds_puzzle = True
            else:
                myObj = array[lower_right[0]][lower_right[1]]
        diagonal_f_ltf_half.update({i : diagonal_str})
        diagonal_f_ltf_half_inverted.update({i : diagonal_str[::-1]})
                
    # second half of diagonal going left to right
    for i in range(1,rows):
        diagonal_str = ''
        myObj = array[i][0]
        exceeds_puzzle = False
        while not exceeds_puzzle:
            lower_right = myObj.get_lower_right_coordinates()
            diagonal_str += myObj.value
            # print(myObj.value,myObj.position, lower_left)
            if lower_right[0] >= rows or lower_right[1] < 0:
                # print('thats the end for me!')
                exceeds_puzzle = True
            else:
                myObj = array[lower_right[0]][lower_right[1]]
        diagonal_s_ltf_half.update({i : diagonal_str})
        diagonal_s_ltf_half_inverted.update({i : diagonal_str[::-1]})
    # print(diagonal_f_ltf_half)
    # print(diagonal_s_ltf_half)
    # print(diagonal_f_ltf_half_inverted)
    # print(diagonal_s_ltf_half_inverted)
    orientations.update({'diagonal_f_ltf_half' : diagonal_f_ltf_half})
    orientations.update({'diagonal_f_ltf_half_inverted' : diagonal_f_ltf_half_inverted})
    orientations.update({'diagonal_s_ltf_half' : diagonal_s_ltf_half})
    orientations.update({'diagonal_s_ltf_half_inverted' : diagonal_s_ltf_half_inverted})
    # print(orientations)
    return orientations
    
    

            
        
        
        
