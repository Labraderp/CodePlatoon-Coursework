# Pad an Array

In this challenge, you'll want to write a method `pad`. It will accept a list, a minimum size (non-negative integer) for the list, and an optional argument of what the list should be "padded" with (see the example with "apple" below).

If the list's length is less than the minimum size, `pad` should return a new list padded with the pad value up to the minimum size.

For example,
```python
pad([1,2,3], 5)
```

should return

```python
[1,2,3,None,None]
```

And

```python
pad([1,2,3], 5, 'apple')
```

should return

```python
[1,2,3,'apple', 'apple']
```

If the minimum size is less than or equal to the length of the list, it should just return the list. That is, `pad([1,2,3], 3)` should return `[1,2,3]`. `pad(my_array, 0)` should always return a list equal to `my_array`.

Remember to write tests!
