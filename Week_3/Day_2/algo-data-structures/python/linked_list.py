class LinkList:
  # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
  def __init__(self, linked_list):
    self.head = linked_list[0]
    self.linked_list = linked_list
    self.length = len(linked_list)

  def add(self, data):
    # write your code to ADD an element to the Linked List
    if self.head == None:
      self.head = data
      self.length += 1

    self.linked_list.append(data)
    self.length += 1
    

  def remove(self, data):
    # write your code to REMOVE an element from the Linked List
    pass

  def get(self, element_to_get):
    # write you code to GET and return an element from the Linked List
    pass

# ----- Node ------
class Node:
  # store your DATA and NEXT values here
  pass
