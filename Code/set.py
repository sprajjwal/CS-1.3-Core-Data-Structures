from hashtable import HashTable

class mySet(object):

  def __init__(self, items=None):
    self.items = HashTable() # setup Hasttable

    # Insert everything
    if items is not None:
            for item in items:
                self.add(item)

  @property
  def size(self):
    """ Makes size an attribute """
    return self.items.length()
  
  def add(self, item):
    """ Insert one item to the set if it doesn't already exist 
    Time complexity: O(1) since we are using hash table
    """
    if not self.items.contains(item): # check if item doesn't exist 
      self.items.set(item, None) # add the item

  def length(self):
    """ Gets the length of the set
    Time complexity: O(1) since we store the length in a property"""
    return self.size

  def is_empty(self):
    """ Checks if the set is empty
    Time complexity: O(1) since we store the length in a property"""
    return self.size == 0

  def contains(self, item):
    """ Checks if item is in the set
    Time Complexity: O(1) since Hash table access is constant time"""
    return self.items.contains(item)

  def remove(self, item):
    """ Check if item exists and remove it or raise Keyerror
    Time complexity: O(1) since accessing from Hashtable is constant time"""
    self.items.delete(item) # remove the item or the inner hashtable will raise error

  def union(self, other_set):
    """ Makes a union with the other set and returns a new set 
    Time complexity: O(n) since getting the keys take linear time"""
    new_set = mySet(self.items.keys())
    for item in other_set.items.keys():
      new_set.add(item)
    return new_set
  
  def intersection(self, other_set):
    """ Makes an intersection between self and other set
    Time complexity: O(n) since calling the keys() takes linear time"""
    a = self.items
    b = other_set.items
    if len(a.keys()) > len(b.keys()):
      a, b = b, a
    new_set = mySet()
    for x in a.keys():
      if b.contains(x):
        new_set.add(x)
    return new_set

  def difference(self, other_set):
    """ Gets the difference between two sets and returns it.
    Time complexity: O(n) since the keys() method takes linear time"""
    return mySet([x for x in self.items.keys() if not other_set.contains(x)])
  
  def is_subset(self, other_set):
    """ Checks if all the items in other_set are in self
    Time complexity: O(n) since we are calling the keys() method that takes linear time"""
    return len(other_set.difference(self).items.keys()) == 0