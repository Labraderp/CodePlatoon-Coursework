# Character Count

For each unique character that appears in the input string, report the number of occurrences of that character in the input. You should return the resulting data as a list of lists. Each list element should be list with in the folowing format:

```python
[<character>, <number of occurrences>]
```

The list should be sorted by the number of occurances (descending). If there is the same number of occurances for two or more characters, then the order should be alphabetical. You can assume that all input will be lower case. Ignore any spaces or punctuation. 

Hint: You'll likely want to use a dictionary to help you solve this!

Examples:

**char_count("aaabbc")**
```python
[
  ["a", 3],
  ["b", 2],
  ["c", 1]
]
```


**char_count("an apple a day will keep the doctor away")**
```python
[
  ["a", 6],
  ["e", 4],
  ["l", 3],
  ["p", 3],
  ["d", 2],
  ["o", 2],
  ["t", 2],
  ["w", 2],
  ["y", 2],
  ["c", 1],
  ["h", 1],
  ["i", 1],
  ["k", 1],
  ["n", 1],
  ["r", 1]
]
```
