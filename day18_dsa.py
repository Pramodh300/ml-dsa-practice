from collections import deque
queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print(queue)

print(queue.popleft())
print(queue)

print(queue[0])

print(len(queue)==0)



class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue.popleft()
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def display(self):
        print(list(self.queue))

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
print(q.peek())


#Circular queue
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear  = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full!")
            return

        if self.is_empty():
            self.front = 0
            self.rear  = 0
        else:
            # wrap around using modulo
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data
        print(f"Enqueued: {data}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!")
            return

        data = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            # only one element was left
            self.front = -1
            self.rear  = -1
        else:
            # wrap around
            self.front = (self.front + 1) % self.size

        return data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty!"
        return self.queue[self.front]

    def display(self):
        print(self.queue)

# Test
cq = CircularQueue(5)
cq.enqueue(1)       # [1, None, None, None, None]
cq.enqueue(2)       # [1, 2, None, None, None]
cq.enqueue(3)       # [1, 2, 3, None, None]
cq.enqueue(4)       # [1, 2, 3, 4, None]
cq.enqueue(5)       # [1, 2, 3, 4, 5]
cq.display()

cq.dequeue()        # removes 1
cq.dequeue()        # removes 2
cq.display()        # [None, None, 3, 4, 5]

cq.enqueue(6)       # wraps around! [None, None, 3, 4, 5] → [6, None, 3, 4, 5]
cq.enqueue(7)       # [6, 7, 3, 4, 5]
cq.display()        # ✅ no space wasted!