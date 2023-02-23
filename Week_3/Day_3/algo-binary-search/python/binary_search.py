def binary_search(value, list_of_values, index=None, result=0):
    print(f'value to find: {value}')
    if len(list_of_values) == 0:
        return -1
    
    if len(list_of_values) == 1:
        if list_of_values[0] == value:
            return index
        return -1
    
    index = round(len(list_of_values) / 2)
    print(f'current index: {index}')
    print(f'current lov: {list_of_values}')
    

    if value == list_of_values[index]:
        print(f'value == list index: {index}')
        return result
    elif value < list_of_values[index]:
        return binary_search(value, list_of_values[0:index], index)
    else:
        result += index
        return binary_search(value, list_of_values[index:len(list_of_values) -1], index)