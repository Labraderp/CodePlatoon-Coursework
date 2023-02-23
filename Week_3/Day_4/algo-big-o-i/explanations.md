## Explanations

Snippet EX-A - Big O: O(n) because as the data set size grows the amount of loop iterations grows linearly
```python
for i in range(1,len(data)):
  print('hello')
```

Snippet EX-B - Big O: O(n) because even though there is a loop inside of a loop here, the inside loop runs a fixed number of times making it constant time, and only the outer loop grows linearly

```python
for i in range(1,len(data)):
  for i in range(10):
    print('hello')
```

Snippet EX-C - Big O: O(n^2) because we have a O(n) loop inside a O(n) loop which means that we multiply them to get O(n^2)
```python
for i in range(1,len(data)):
  for i in range(1, len(data)):
    print('hello')
```

Snippet EX-D - Big O: O(n^2) because in the worst case (i=1) the inner loop runs O(n) times and the outer loop runs O(n), which we multiply to be O(n^2)
```python
for i in range(1, len(data)):
  for j in range(j, len(data)):
    print(i)
```

Snippet EX-E - Big O: O(n * m) because the two loops do not depend on each other but both run linearly in time
```python 
for i in range(1,len(data)):
  for i in range(1, len(other_data)):
    print('hello')

```

Snippet EX-F - Big O: O(n * m) because for every element in the data array (n) we must visit every element in the dictionary for that element (m).

```python
for dictionary in array:
  for key, value in dictionary.items():
    print(f"{key} maps to {value}")
```

Snippet EX-G - Big O: O(n) because in order to get all the keys in the dictionary, we must visit every element one time, which is a linear operation
```ruby
print(dictionary.keys())
```

Snippet EX-H - Big O: O(n) because the first set of nested loops is O(n) * O(1) = O(n) and then the next sequential loop is also O(n), but because they are not nested, we just choose the 'worst' case (though they are the same in this case)
```python
for item in data:
  for in range(3):
    print(item)

for item in data:
  print('hello')
```
