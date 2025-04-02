class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def append(self, element: str) -> None:
        new_node = Node(element)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")

        new_node = Node(element)
        if index == 0:
            if self.head is None:
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.size:
            self.append(element)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

        self.size += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        if index == 0:
            deleted_value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        elif index == self.size - 1:
            deleted_value = self.tail.value
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            deleted_value = current.value
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

        self.size -= 1
        return deleted_value

    def deleteAll(self, element: str) -> None:
        current = self.head
        while current:
            if current.value == element:
                self.delete(self.findFirst(element))
            current = current.next

    def get(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def clone(self) -> "DoublyLinkedList":
        cloned_list = DoublyLinkedList()
        current = self.head
        while current:
            cloned_list.append(current.value)
            current = current.next
        return cloned_list

    def reverse(self) -> None:
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def findFirst(self, element: str) -> int:
        current = self.head
        index = 0
        while current:
            if current.value == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: str) -> int:
        current = self.tail
        index = self.size - 1
        while current:
            if current.value == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = self.tail = None
        self.size = 0

    def extend(self, elements: "DoublyLinkedList") -> None:
        current = elements.head
        while current:
            self.append(current.value)
            current = current.next

    def print_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print(f"List: {elements}")