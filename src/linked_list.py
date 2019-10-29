# Implement linkedlist


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_to_head(self, value):
        if self.head:
            self.head = Node(value, self.head)
            return

        self.head = Node(value)

    def remove(value):
        if self.head is Node:
            print("Error: value not found.")
            return
        elif self.head.value == value:
            node_value = self.head.value
            self.head = self.head.next

            return node_value
        else:

            prev_node = self.head
            current_node = self.head.next

            while current_node:
                if current_node.value == value:

                    return value
                current_node = current_node.next
