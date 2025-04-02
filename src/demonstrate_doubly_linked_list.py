from doubly_linked_list import DoublyLinkedList

def demonstrate_length():
    lst = DoublyLinkedList()
    print(f"Initial length: {lst.length()}")
    lst.append('a')
    print(f"Length after adding an element: {lst.length()}")

def demonstrate_append():
    lst = DoublyLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.print_list()

def demonstrate_insert():
    lst = DoublyLinkedList()
    lst.append('a')
    lst.append('c')
    lst.insert('b', 1)
    lst.print_list()

def demonstrate_delete():
    lst = DoublyLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    deleted_element = lst.delete(1)
    print(f"Deleted element '{deleted_element}' at position 1: ", end="")
    lst.print_list()

def demonstrate_deleteAll():
    lst = DoublyLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('a')
    lst.deleteAll('a')
    lst.print_list()

def demonstrate_get():
    lst = DoublyLinkedList()
    lst.append('x')
    lst.append('y')
    print(f"Element at index 1: {lst.get(1)}")

def demonstrate_clone():
    lst = DoublyLinkedList()
    lst.append('a')
    lst.append('b')
    cloned_lst = lst.clone()
    print(f"Original list: ", end="")
    lst.print_list()
    print(f"Cloned list: ", end="")
    cloned_lst.print_list()

def demonstrate_reverse():
    lst = DoublyLinkedList()
    lst.append('a')
    lst.append('b')
    lst.append('c')
    lst.reverse()
    lst.print_list()

def demonstrate_findFirst():
    lst = DoublyLinkedList()
    lst.append('x')
    lst.append('y')
    lst.append('x')
    index = lst.findFirst('x')
    print(f"First occurrence of 'x' at index: {index}")

def demonstrate_findLast():
    lst = DoublyLinkedList()
    lst.append('x')
    lst.append('y')
    lst.append('x')
    index = lst.findLast('x')
    print(f"Last occurrence of 'x' at index: {index}")

def demonstrate_clear():
    lst = DoublyLinkedList()
    lst.append('x')
    lst.append('y')
    lst.clear()
    lst.print_list()

def demonstrate_extend():
    lst1 = DoublyLinkedList()
    lst1.append('a')
    lst1.append('b')

    lst2 = DoublyLinkedList()
    lst2.append('x')
    lst2.append('y')

    lst1.extend(lst2)
    lst1.print_list()


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