array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

char_arr = ['b', 'a', 'n', 'a', 'n', 'a', 's']

def linear_search(value_to_find, array_to_search_through):
    for number in range(len(array_to_search_through)):
        if array_to_search_through[number] == value_to_find:
            return number
        
    return None

def linear_search_global(value_to_find, array_to_search_through):
    results = []
    for number in range(len(array_to_search_through)):
        if array_to_search_through[number] == value_to_find:
            results.append(number)
    
    if len(results) == 0:
        return None
    else:
        return results

print(linear_search(400, array_to_search_through))
print(linear_search_global('n', char_arr))