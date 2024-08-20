class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def reverse(self):
        temp = self.head
        while temp is not None:
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
            
        self.head, self.tail = self.tail, self.head