import unittest

from src.based_list import BasedList

class TestBasedList(unittest.TestCase):

    def setUp(self):
        """Initialize a new BasedList before each test."""
        self.lst = BasedList()

    def test_length(self):
        """Test length method with an empty and non-empty list."""
        self.assertEqual(self.lst.length(), 0)
        self.lst.append('a')
        self.assertEqual(self.lst.length(), 1)
        self.lst.append('b')
        self.lst.append('c')
        self.assertEqual(self.lst.length(), 3)

    def test_append(self):
        """Test appending elements to the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.data, ['a', 'b'])
        self.lst.append('c')
        self.assertEqual(self.lst.data, ['a', 'b', 'c'])

    def test_insert(self):
        """Test inserting elements at valid and invalid indices."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.insert('x', 1)
        self.assertEqual(self.lst.data, ['a', 'x', 'b'])

        self.lst.insert('y', 0)
        self.assertEqual(self.lst.data, ['y', 'a', 'x', 'b'])

        self.lst.insert('z', self.lst.length())
        self.assertEqual(self.lst.data, ['y', 'a', 'x', 'b', 'z'])

        with self.assertRaises(IndexError):
            self.lst.insert('w', -1)

        with self.assertRaises(IndexError):
            self.lst.insert('t', 10)

    def test_delete(self):
        """Test deleting elements by index."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        deleted = self.lst.delete(1)
        self.assertEqual(deleted, 'b')
        self.assertEqual(self.lst.data, ['a', 'c'])

        with self.assertRaises(IndexError):
            self.lst.delete(5)

        with self.assertRaises(IndexError):
            self.lst.delete(-1)

        # Deleting last element
        self.lst.delete(1)
        self.assertEqual(self.lst.data, ['a'])

        # Deleting the only element
        self.lst.delete(0)
        self.assertEqual(self.lst.data, [])

    def test_deleteAll(self):
        """Test deleting all occurrences of an element."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.lst.append('c')
        self.lst.deleteAll('a')
        self.assertEqual(self.lst.data, ['b', 'c'])

        # Deleting an element not in the list should not change it
        self.lst.deleteAll('x')
        self.assertEqual(self.lst.data, ['b', 'c'])

    def test_get(self):
        """Test getting elements by index."""
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.get(1), 'b')

        with self.assertRaises(IndexError):
            self.lst.get(10)

        with self.assertRaises(IndexError):
            self.lst.get(-1)

    def test_clone(self):
        """Test cloning a list."""
        self.lst.append('a')
        self.lst.append('b')
        cloned_lst = self.lst.clone()
        self.assertEqual(cloned_lst.data, self.lst.data)
        self.assertIsNot(cloned_lst, self.lst)

        # Ensure modifications to the original do not affect the clone
        self.lst.append('c')
        self.assertNotEqual(cloned_lst.data, self.lst.data)

    def test_reverse(self):
        """Test reversing a list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.reverse()
        self.assertEqual(self.lst.data, ['c', 'b', 'a'])

        # Reverse an empty list
        empty_lst = BasedList()
        empty_lst.reverse()
        self.assertEqual(empty_lst.data, [])

    def test_findFirst(self):
        """Test finding the first occurrence of an element."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.assertEqual(self.lst.findFirst('a'), 0)
        self.assertEqual(self.lst.findFirst('b'), 1)
        self.assertEqual(self.lst.findFirst('x'), -1)

        # Finding in an empty list
        empty_lst = BasedList()
        self.assertEqual(empty_lst.findFirst('a'), -1)

    def test_findLast(self):
        """Test finding the last occurrence of an element."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.assertEqual(self.lst.findLast('a'), 2)
        self.assertEqual(self.lst.findLast('b'), 1)
        self.assertEqual(self.lst.findLast('x'), -1)

        # Finding in an empty list
        empty_lst = BasedList()
        self.assertEqual(empty_lst.findLast('a'), -1)

    def test_clear(self):
        """Test clearing the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.clear()
        self.assertEqual(self.lst.data, [])

        # Clearing an already empty list should not cause errors
        self.lst.clear()
        self.assertEqual(self.lst.data, [])

    def test_extend(self):
        """Test extending a list with another BasedList."""
        self.lst.append('a')
        self.lst.append('b')

        lst2 = BasedList()
        lst2.append('x')
        lst2.append('y')

        self.lst.extend(lst2)
        self.assertEqual(self.lst.data, ['a', 'b', 'x', 'y'])
        self.assertEqual(lst2.data, ['x', 'y'])

        # Extending with an empty list
        empty_lst = BasedList()
        self.lst.extend(empty_lst)
        self.assertEqual(self.lst.data, ['a', 'b', 'x', 'y'])

        empty_lst.extend(lst2)
        self.assertEqual(empty_lst.data, ['x', 'y'])

if __name__ == '__main__':
    unittest.main()