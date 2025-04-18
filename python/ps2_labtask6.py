class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.max_size = size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.max_size == self.front:
            print("Overflow: Queue is full.")
            return
        if self.front == -1:  # First element
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            print("Underflow: Queue is empty.")
            return
        value = self.queue[self.front]
        if self.front == self.rear:  # Last element
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return value

    def display(self):
        if self.front == -1:
            print("Queue is empty.")
            return
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.max_size
        print()

# Example Usage:
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.dequeue()
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)  # Should show overflow
cq.display()
