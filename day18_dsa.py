from collections import deque
'''queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)
print(queue)

print(queue.popleft())
print(queue)

print(queue[0])

print(len(queue)==0)
'''


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