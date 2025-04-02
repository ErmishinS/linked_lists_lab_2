from based_list import BasedList


def demonstrate_length():
    lst = BasedList()
    print(f"Initial length: {lst.length()}")
    lst.append('a')
    print(f"Length after adding an element: {lst.length()}")

def demonstrate_append():
    lst = BasedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    print(f"List after appending elements: {lst.data}")

def demonstrate_insert():
    lst = BasedList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    print(f"List after inserting 'b' at position 1: {lst.data}")

def demonstrate_delete():
    lst = BasedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    deleted_element = lst.delete(1)
    print(f"Deleted element '{deleted_element}' at position 1: {lst.data}")

def demonstrate_deleteAll():
    lst = BasedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    lst.deleteAll('a')
    print(f"List after deleting all occurrences of 'a': {lst.data}")

def demonstrate_get():
    lst = BasedList()
    lst.append('x')
    lst.append('y')
    print(f"Element at index 1: {lst.get(1)}")

def demonstrate_clone():
    lst = BasedList()
    lst.append('a')
    lst.append('b')
    cloned_lst = lst.clone()
    print(f"Original list: {lst.data}")
    print(f"Cloned list: {cloned_lst.data}")

def demonstrate_reverse():
    lst = BasedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.reverse()
    print(f"List after reversing: {lst.data}")

def demonstrate_findFirst():
    lst = BasedList()
    lst.append('x')
    lst.append('y')
    lst.append('x')
    index = lst.findFirst('x')
    print(f"First occurrence of 'x' at index: {index}")

def demonstrate_findLast():
    lst = BasedList()
    lst.append('x')
    lst.append('y')
    lst.append('x')
    index = lst.findLast('x')
    print(f"Last occurrence of 'x' at index: {index}")

def demonstrate_clear():
    lst = BasedList()
    lst.append('x')
    lst.append('y')
    lst.clear()
    print(f"List after clearing: {lst.data}")

def demonstrate_extend():
    lst1 = BasedList()
    lst1.append('a')
    lst1.append('b')

    lst2 = BasedList()
    lst2.append('x')
    lst2.append('y')

    lst1.extend(lst2)
    print(f"List after extending: {lst1.data}")

# Run all demonstrations
demonstrate_length()
demonstrate_append()
demonstrate_insert()
demonstrate_delete()
demonstrate_deleteAll()
demonstrate_get()
demonstrate_clone()
demonstrate_reverse()
demonstrate_findFirst()
demonstrate_findLast()
demonstrate_clear()
demonstrate_extend()