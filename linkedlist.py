class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete the first occurrence of a node with specified data
    def delete(self, data):
        current = self.head
        previous = None
        while current and current.data != data:
            previous = current
            current = current.next
        if not current:
            print(f"Node with data {data} not found.")
            return
        if previous:
            previous.next = current.next
        else:
            self.head = current.next

# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None
ll.delete(2)
ll.display()  # Output: 1 -> 3 -> None
