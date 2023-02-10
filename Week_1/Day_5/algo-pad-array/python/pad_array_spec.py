from pad_array import pad

# Curious? Learn more about `None` in Python:
# https://docs.python.org/3/library/constants.html
# https://www.pythontutorial.net/advanced-python/python-none/
print(pad([1,2,3], 5) == [1,2,3, None, None])
print(pad([1,2,3], 'apple') == [1,2,3], 'apple', 'apple'])
print(pad([1,2,3], 3) == [1,2,3])

# Challenge - what edge case do we NOT have tests for? Add a test for it, and any other tests you think will increase our test coverage
# for the possible valid inputs our program might receive.
