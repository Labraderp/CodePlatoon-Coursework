# Data Structures

## This challenge will help you to:
- Know what a data structure is
- Learn the different types of data structures and the main operations/methods associated with each
- Construct each data structure

## Summary
We're going to create several data structures and the methods most commonly used for that data structure using Object Oriented Programming.

### READING DOCUMENTATION IS KEY THROUGHOUT YOUR CAREER (80% reading, 20% coding)

## What is a Data Structure?

“In computer science, a data structure is a data organization, management, and storage format that enables efficient access and modification. __More precisely, a data structure is a collection of data values, the relationships among them within computer memory, and the functions or operations that can be applied to the data.__”


## Construct a Stack, Queue, and Linked List
(Please Watch The Video Links)
- [Stacks & Queues](https://youtu.be/wjI1WNcIntg) (Stacks are LIFO "Last in, First out" and have `push` and `pop` methods. Queues are FIFO "First in, First out" and have `enqueue` and `dequeue` methods)
- [Linked Lists](https://youtu.be/njTh_OwMljA) (Linked Lists utilize `Nodes` at each individual 'point' in the Linked list. Each `Node` has a `data` value and `next` value that points to the next `Node`. Linked Lists have an `insert`, `remove`, `display`, and `search` methods)
### Linked List
A Link List is a collection of _Nodes_ (a basic unit of a data structure) that contains data, the `data` or  `value` of the _Node_, and a `next` value that points to the next _Node_ in the Linked List. Note: __Nodes__ may contain different data depending on the type of Data Structure it exists in. i.e. A __Node__ in a Linked List contains different data than a Binary Search Tree. 

```
Head of the Linked List -> Node A
Node A has a value of 23 and a pointer to the next Node -> Node B
Node B has a value of 78 and a pointer to the next Node -> Node C
Node C has a value of 46 and a pointer to the next Node -> null/None (there is no next Node)
```

A Node is a Class seperate from a Linked List Class. A Linked List has many Nodes.

### Construct a Node Class in your linked_list.py file.
<details><summary>Click here for a Hint</summary>
<p>

__Node Example in Python__
```python
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
```
</p>
</details>


### Construct the __init__ method for your Linked List in the linked_list.py file.
<details><summary>Click here for a Hint</summary>
<p>

__Here is the basic Class structure of a Linked List in Python__
```python
class LinkList():
  def __init__(self, head=None):
    self.head = head
    self.length # we're going to store the length of the Linked List here

  def add(self, data):
    # write your code to ADD an element to the Linked List
    pass

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    pass

  def get(self, element):
    # write you code to GET and return an element from the Linked List
    pass

# ---- Node -----
class Node():
  # your __init__ method here

```
</p>
</details>

## STRETCH GOAL: Construct a Binary Search Tree and a Hash Table
(Please Watch The Video Links)

__[Binary Tree/Binary Search Tree](https://youtu.be/D5SrAga1pno):__ (BSTs utilze `Nodes` at each individual point in the BST. Each `Node` has a `key` or `data` value, a `left` value, and a `right` value. The `left` and `right` values point to the `Node` to the left and right of them on the Tree. Binary Search Trees have an `insert`, `delete`, and `search` method)
![BST Example](https://github.com/oscarplatoon/curriculum/blob/master/page-resources/bst.png)

A classic problem for trees is how to traverse them — i.e., visit and process every node. There are four flavors of tree traversal:

__Breadth-first:__ start at level 0, then go through all nodes at level 1, then all nodes at level 2, etc. This is meaningful when tree level actually has some meaning; for example, a hierarchical org chart. It is less useful for a BST, where levels don't usually have intrinsic meaning.

__Depth-first:__ go down paths to certain stopping points before moving on to the next branch. Three types:
pre-order: process the current node value, then go down the left branch, then the right branch. 

* in-order: process all the left children (lesser values), then this node's value, then the right children (greater values). This is the most useful for a BST as it respects the intrinsic ordering of the tree; values are processed from smallest to greatest.
* post-order: process all the left children, then right children, then this node's value. This processes leaves before parents, so can be used in languages with explicit memory management to delete nodes in a safe way.


## Hash Table
__[Hash Table](https://youtu.be/h2d9b_nEzoA):__ [Overview](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/) - A Hash Table converts a string value to a numberic `key` value. The value of the `key` is the index of the Hash Table where the string value is stored.
#### Hash function example steps
```python
# - Think of a Hash Table is an array that is of a fixed length, lets say a length 35
# - [None, None, None....] an array of 35 indexes that are initially empty
# - A Hash Table has a HASH function that converts the input_value that you want to store into a numeric value.
# - The numberic value is the index of the Hash Table where your input_value is stored

# - Your hash function is within your HashTable class
def hash(self, string_value):
  # Step 1: Turn the string_value to a numeric value
  # Step 2: Divide the numberic value by the size of the Hash Table and return that value
```
![Hash Visualization](https://github.com/oscarplatoon/curriculum/blob/master/page-resources/hash_visualization.png)

# Challenge

### Construct a Queue, Stack, Binary Search Tree, and a Hash Table in the respective Python Files

## Resources
* [Fundamentals Explaned](https://www.interviewcake.com/article/python/data-structures-coding-interview)
