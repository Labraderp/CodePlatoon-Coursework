# import the functions `linear_search` and `linear_search_global` from linear_search.py
from linear_search import linear_search,linear_search_global

# helper function that compares two arrays and returns `True` if the lists are equivalent
def compareArrays (array1, array2):

    if len(array1) != len(array2):
        return False
   
    for element in array1:
        
        if element not in array2:
            return False
  
    return True

# tests for linear_search
print(linear_search(3, [1,2,3]) == 2)
print(linear_search(4, [1,2,3]) == None)
print(linear_search(13, [1,2,3]) == None)

# tests for linear_search_global
print(compareArrays(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]), [1, 3, 5]))
print(compareArrays(linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]), [6]))
print(compareArrays(linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]), [2, 4]))