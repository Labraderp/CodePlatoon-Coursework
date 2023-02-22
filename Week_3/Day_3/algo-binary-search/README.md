# Binary Search

The goal is to find the index of a value that you pass in compared to a sorted array of strings or integers. You can read more [here](https://en.wikipedia.org/wiki/Binary_search_algorithm).

Let's take a look at some code:

```python
values = random.sample(list(range(1,10000)), 1000)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

binary_search(537, values) # this returns the index of 537 in values if it exists and -1 if it doesn't exist
```

Here's the basic premise of the algorithm:

1. Say you're searching for a value `number_to_find` in a search set of `sorted_values`
2. Find the middle value in `sorted_values` we'll call `middle_value`
3. If `number_to_find` is equal to `middle_value` then your target is found
4. If `number_to_find` is less than `middle_value`, split your `sorted_values` in half and repeat the algorithm on your new subset (the half of `sorted_values` before `middle_value`)
5. If `number_to_find` is greater than `middle_value`, repeat step but with the half of `sorted_values `values` after `middle_value`
6. Repeat until you find `number_to_find` or return `-1` if it doesn't exist

