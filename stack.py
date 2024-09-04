class Stack:
    def __init__(self):
        self.stack = []

    # Push operation: Add an element to the top of the stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} onto the stack.")

    # Pop operation: Remove and return the top element of the stack
    def pop(self):
        if not self.is_empty():
            removed_item = self.stack.pop()
            print(f"Popped {removed_item} from the stack.")
            return removed_item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    # Peek operation: View the top element without removing it
    def peek(self):
        if not self.is_empty():
            print(f"Top element is {self.stack[-1]}")
            return self.stack[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# Example usage
stack = Stack()
stack.push(1)

stack.peek()
stack.pop()
stack.peek()
# Trying to pop from an empty stack

