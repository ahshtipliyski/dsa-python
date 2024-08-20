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

    def swap_first_last(self):
        if self.length <= 1:
            return None
        else:
            tempValue1 = self.head.value
            tempValue2 = self.tail.value
            self.head.value = tempValue2
            self.tail.value = tempValue1
            return True
        
        # if self.head is None or self.head == self.tail:
        #     return
        # self.head.value, self.tail.value = self.tail.value, self.head.value