def manipulate(array):
    rows = len(array)
    cols = len(array[0])
    # print(f'rows are {rows}')
    # print(f'cols are {cols}')
    
    orientations = {}
    #print horizontal arrays
    horizontal = {}
    for index, row in enumerate(array):
        # print(f"{([item.value for item in row])}")
        horizontal.update({index : ''.join([item.value for item in row])})
    print(horizontal)