from set import mySet
import unittest

class StackTest(unittest.TestCase):

    def test_init(self):
      s = mySet()
      assert s.length() == 0
      assert s.is_empty() is True

    def test_init_with_list(self):
      s = mySet(['A', 'B', 'C', 'D'])
      assert s.length() == 4
      assert s.is_empty() is False

    def test_add(self):
      s = mySet()
      s.add(1)
      assert s.length() == 1
      assert s.is_empty() is False
      s.add(1)
      assert s.length() == 1
      assert s.is_empty() is False
      s.add(2)
      assert s.length() == 2
      assert s.is_empty() is False

    def test_length(self):
      s = mySet()
      s.add(1)
      assert s.length() == 1
      s.add(2)
      assert s.length() == 2
      s.remove(1)
      assert s.length() == 1

    def test_contains(self):
      s = mySet([1, 2, 3, 4])
      assert s.length() == 4
      assert s.contains(1) == True
      assert s.contains(2) == True
      assert s.contains(3) == True
      assert s.contains(4) == True
      assert s.contains(5) == False
      s.remove(2)
      assert s.contains(2) == False

    def test_union(self):
      s1 = mySet([1, 2, 3, 4])
      s2 = mySet([3, 4, 5, 6])
      s3 = s1.union(s2)
      assert s3.items.keys() == [1, 2, 3, 4, 5, 6]
      assert s3.length() == 6

    def test_intersection(self):
      s1 = mySet([1, 3, 4])
      s2 = mySet([3, 4, 5, 6])
      s3 = s1.intersection(s2)
      assert s3.items.keys() == [3, 4]
      assert s3.length() == 2
      s4 = s2.intersection(s1)
      assert s4.items.keys() == [3, 4]
      assert s4.length() == 2

    def test_difference(self):
      s1 = mySet([1,2, 3, 4])
      s2 = mySet([3, 4, 5, 6])
      s3 = s1.difference(s2)
      assert s3.items.keys() == [1, 2]
      assert s3.length() == 2

    def test_is_subset(self):
      s1 = mySet([1, 2, 3, 4])
      s2 = mySet([2, 3])
      assert s1.is_subset(s2) == True
      assert s2.is_subset(s1) == False