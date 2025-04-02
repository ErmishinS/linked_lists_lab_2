import unittest
from src.doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        """Initialize a new DoublyLinkedList before each test."""
        self.lst = DoublyLinkedList()

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
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a', 'b'])
        self.lst.append('c')
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a', 'b', 'c'])

    def test_insert(self):
        """Test inserting elements at valid and invalid indices."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.insert('x', 1)
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a', 'x', 'b'])

        self.lst.insert('y', 0)
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['y', 'a', 'x', 'b'])

        self.lst.insert('z', self.lst.length())
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['y', 'a', 'x', 'b', 'z'])

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
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a', 'c'])

        with self.assertRaises(IndexError):
            self.lst.delete(5)

        with self.assertRaises(IndexError):
            self.lst.delete(-1)

        # Deleting last element
        self.lst.delete(1)
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a'])

        # Deleting the only element
        self.lst.delete(0)
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], [])

    def test_deleteAll(self):
        """Test deleting all occurrences of an element."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.lst.append('c')
        self.lst.deleteAll('a')
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['b', 'c'])

        # Deleting an element not in the list should not change it
        self.lst.deleteAll('x')
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['b', 'c'])

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
        self.assertEqual([node.value for node in self._iterate(cloned_lst.head)], ['a', 'b'])
        self.assertIsNot(cloned_lst, self.lst)

        # Ensure modifications to the original do not affect the clone
        self.lst.append('c')
        self.assertNotEqual([node.value for node in self._iterate(cloned_lst.head)], [node.value for node in self._iterate(self.lst.head)])

    def test_reverse(self):
        """Test reversing a list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.reverse()
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['1234567890'])

        # Reverse an empty list
        empty_lst = DoublyLinkedList()
        empty_lst.reverse()
        self.assertEqual([node.value for node in self._iterate(empty_lst.head)], [])

    def test_findFirst(self):
        """Test finding the first occurrence of an element."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.assertEqual(self.lst.findFirst('a'), 0)
        self.assertEqual(self.lst.findFirst('b'), 1)
        self.assertEqual(self.lst.findFirst('x'), -1)

        # Finding in an empty list
        empty_lst = DoublyLinkedList()
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
        empty_lst = DoublyLinkedList()
        self.assertEqual(empty_lst.findLast('a'), -1)

    def test_clear(self):
        """Test clearing the list."""
        self.lst.append('a')
        self.lst.append('b')
        self.lst.clear()
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], [])

        # Clearing an already empty list should not cause errors
        self.lst.clear()
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], [])

    def test_extend(self):
        """Test extending a list with another DoublyLinkedList."""
        self.lst.append('a')
        self.lst.append('b')

        lst2 = DoublyLinkedList()
        lst2.append('x')
        lst2.append('y')

        self.lst.extend(lst2)
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a', 'b', 'x', 'y'])
        self.assertEqual([node.value for node in self._iterate(lst2.head)], ['x', 'y'])

        # Extending with an empty list
        empty_lst = DoublyLinkedList()
        self.lst.extend(empty_lst)
        self.assertEqual([node.value for node in self._iterate(self.lst.head)], ['a', 'b', 'x', 'y'])

        empty_lst.extend(lst2)
        self.assertEqual([node.value for node in self._iterate(empty_lst.head)], ['x', 'y'])

    def _iterate(self, head):
        """Helper method to iterate through the list and return node values."""
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next
        return nodes

if __name__ == '__main__':
    unittest.main()