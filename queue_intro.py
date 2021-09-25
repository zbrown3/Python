from node_doubly_linked import Node

class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size = None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

  def enqueue(self, value):
    if self.has_space() == True:
      item_to_add = Node(value)
      print("Adding {} to the queue!".format(str(item_to_add.get_value())))
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")

  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
    
  def peek(self):
    if self.get_size() == 0:
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size

  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    if self.size == 0:
      return True
    else:
      return False