import unittest

from src.based_list import BasedList

class TestBasedList(unittest.TestCase):

    def setUp(self):
        """Initialize a new BasedList before each test."""
        self.lst = BasedList()

    def test_length(self):
        self.assertEqual(self.lst.length(), 0)
        self.lst.append('a')
        self.assertEqual(self.lst.length(), 1)

    def test_append(self):
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.data, ['a', 'b'])

    def test_insert(self):
        self.lst.append('a')
        self.lst.append('b')
        self.lst.insert('x', 1)
        self.assertEqual(self.lst.data, ['a', 'x', 'b'])

        with self.assertRaises(IndexError):
            self.lst.insert('y', -1)

        with self.assertRaises(IndexError):
            self.lst.insert('z', 10)

    def test_delete(self):
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

    def test_deleteAll(self):
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.lst.append('c')
        self.lst.deleteAll('a')
        self.assertEqual(self.lst.data, ['b', 'c'])

    def test_get(self):
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.get(1), 'b')

        with self.assertRaises(IndexError):
            self.lst.get(10)

        with self.assertRaises(IndexError):
            self.lst.get(-1)

    def test_clone(self):
        self.lst.append('a')
        self.lst.append('b')
        cloned_lst = self.lst.clone()
        self.assertEqual(cloned_lst.data, self.lst.data)
        self.assertIsNot(cloned_lst, self.lst)

    def test_reverse(self):
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('c')
        self.lst.reverse()
        self.assertEqual(self.lst.data, ['c', 'b', 'a'])

    def test_findFirst(self):
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.assertEqual(self.lst.findFirst('a'), 0)
        self.assertEqual(self.lst.findFirst('b'), 1)
        self.assertEqual(self.lst.findFirst('x'), -1)

    def test_findLast(self):
        self.lst.append('a')
        self.lst.append('b')
        self.lst.append('a')
        self.assertEqual(self.lst.findLast('a'), 2)
        self.assertEqual(self.lst.findLast('b'), 1)
        self.assertEqual(self.lst.findLast('x'), -1)

    def test_clear(self):
        self.lst.append('a')
        self.lst.append('b')
        self.lst.clear()
        self.assertEqual(self.lst.data, [])

    def test_extend(self):
        self.lst.append('a')
        self.lst.append('b')

        lst2 = BasedList()
        lst2.append('x')
        lst2.append('y')

        self.lst.extend(lst2)
        self.assertEqual(self.lst.data, ['a', 'b', 'x', 'y'])
        self.assertEqual(lst2.data, ['x', 'y'])  # Ensure lst2 remains unchanged

if __name__ == '__main__':
    unittest.main()