#Create linked list
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

current = head
while current:
    print(current.data)
    current = current.next



#Count nodes
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
count = 0

current = head
while current:
    count += 1
    current = current.next
print(count)



#Search element
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c


head = a
target = 20
current = head
found = False

while current:
    if current.data == target:
        found = True
        break
    current = current.next
print(found)



#Insert at Beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

head = a

current = head
while current:
    print(current.data)
    current = current.next

new = Node(5)
new.next = head
head = new

current = head
while current:
    print(current.data)
    current = current.next



#Insert at end
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(1)
b = Node(2)


a.next = b

head = a

new = Node(3)

current = head
while current.next:
    current = current.next
current.next = new

current = head
while current:
    print(current.data)
    current = current.next

    

#Delete node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)

a.next = b
b.next = c

head = a

current = head
while current:
    print(current.data)
    current = current.next

current = head
target = 20
while current.next:
    if current.next.data == target:
        current.next = current.next.next
        break
    
    current = current.next

print("After deleting")
current = head
while current:
    print(current.data)
    current = current.next