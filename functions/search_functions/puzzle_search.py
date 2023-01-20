import re

import functions.setup_functions.puzzle_setup as setup_f
import functions.search_functions.orientation_mainpulator as om

array = setup_f.setup('use')
conts = array[1]

def search_single(keyword):
    # print(array)
    if array: #to make sure it is not empty
        match_list = []
        key_to_pass = None
        index_to_pass = None
        span_to_pass = None
        # words = array[2]
        manipulated_obj = om.manipulate(conts)
        for key in manipulated_obj:
            for i in manipulated_obj[key]:
                # print(f'{key}, {i}, {manipulated_obj[key][i]}')
                match = re.search(keyword, manipulated_obj[key][i])
                if match:
                # if manipulated_obj[key][i] == keyword:
                    key_to_pass = key
                    index_to_pass = i
                    span_to_pass = match.span()
                    print(f'Found it!, it is at {key}, {i}, {match.span()}')
                    #for repeating words
                    match_list.append([keyword, key_to_pass, index_to_pass, span_to_pass])
                    # print(match.span())
        if key_to_pass and index_to_pass is not None and span_to_pass:
            process_answer(match_list)
            # process_answer(keyword, key_to_pass, index_to_pass, span_to_pass)
        else:
            raise Exception('you are looking for a word that is not in the list of words')

def process_answer(match_list):
    for match in match_list:
        keyword = match[0]
        key = match[1]
        index = match[2]
        span = match[3]

        if key == 'horizontal':
            copy_arr = conts
            for i in range(span[0], span[1]):
                copy_arr[index][i].value = '_'
            print(f'\n{keyword} starts @ row {index+1} column {span[0]+1}, going to the right until column {span[1]}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'horizontal_inverted':
            copy_arr = conts
            col_len = len(copy_arr[0])
            for i in range(span[0], span[1]):
                copy_arr[index][-(i+1)].value = '_'
            print(f'\n{keyword} starts @ row {index+1} column {col_len - span[0]}, going to the left until column {col_len - span[1]+1}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'vertical':
            copy_arr = conts
            for i in range(span[0], span[1]):
                copy_arr[i][index].value = '_'
            print(f'\n{keyword} starts @ row {span[0]} column {index+1}, going up until row {span[1]}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'vertical_inverted':
            copy_arr = conts
            col_len = len(copy_arr[0])
            for i in range(span[0], span[1]):
                copy_arr[-(i+1)][index].value = '_'
            print(f'\n{keyword} starts @ row {col_len - span[0]} column {index+1}, going down until row {col_len - span[1]}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'diagonal_f_half':
            copy_arr = conts
            curr_row = span[0]
            curr_col = index
            final_index = 0
            for i in range(span[0], span[1]):
                copy_arr[curr_row + i][curr_col - i].value = '_'
                final_index = i
            print(f'\n{keyword} starts @ row {span[0]+1} column {index+1}, going down diagonally to row {curr_row + final_index + 1} col {curr_col - final_index + 1}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'diagonal_f_half_inverted':
            pass
        elif key == 'diagonal_s_half':
            pass
        elif key == 'diagonal_s_half_inverted':
            pass
        elif key == 'diagonal_f_ltf_half':
            copy_arr = conts
            curr_row = span[0]
            curr_col = index
            final_index = 0
            for i in range(span[0], span[1]):
                copy_arr[curr_row + i][curr_col + i].value = '_'
                final_index = i
            print(f'\n{keyword} starts @ row {span[0]+1} column {index+1}, going down diagonally to row {curr_row + final_index + 1} col {curr_col + final_index + 1}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'diagonal_f_ltf_half_inverted':
            pass
        elif key == 'diagonal_s_ltf_half':
            copy_arr = conts
            curr_row = span[0]+1
            curr_col = index-1
            final_index = 0
            for i in range(span[0], span[1]):
                copy_arr[curr_row + i][curr_col + i].value = '_'
                final_index = i
            print(f'\n{keyword} starts @ row {span[0]+2} column {index}, going down diagonally to row {curr_row + final_index + 1} col {curr_col + final_index + 1}\n')
            for line in copy_arr:
                print(f"\t{'   '.join([item.value for item in line])}\n")
        elif key == 'diagonal_s_ltf_half_inverted':
            pass
        else:
            print('Sorry, we were not able to find your word :(')
            raise Exception('key passed is non existent')



    





