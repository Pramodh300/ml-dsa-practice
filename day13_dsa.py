#Reverse linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

head = a

prev = None
current = head

while current:
    nxt = current.next
    current.next = prev

    prev = current
    current = nxt
head = prev
current = head
while current:
    print(current.data)
    current = current.next