class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation: Add an element to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued {item} to the queue.")

    # Dequeue operation: Remove and return the front element of the queue
    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.pop(0)
            print(f"Dequeued {removed_item} from the queue.")
            return removed_item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    # Peek operation: View the front element without removing it
    def peek(self):
        if not self.is_empty():
            print(f"Front element is {self.queue[0]}")
            return self.queue[0]
        else:
            print("Queue is empty. Nothing to peek.")
            return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

# Example usage
queue = Queue()
queue.enqueue(1)

queue.peek()
queue.dequeue()
queue.peek()
