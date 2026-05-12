#Merge two lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''def merge_sorted_lists(head1, head2):
    dummy = Node(0)

    current = dummy
    p1 = head1
    p2 = head2

    while p1 and p2:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next

        else:
            current.next = p2
            p2 = p2.next
        current = current.next

    if p1:
        current.next = p1
    if p2:
        current.next = p2

    return dummy.next

def print_ll(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("None")



n1 = Node(1);
n2 = Node(3);
n3 = Node(5)

n1.next = n2
n2.next = n3

n4 = Node(2);
n5 = Node(4);
n6 = Node(6)

n4.next = n5
n5.next = n6

merged = merge_sorted_lists(n1, n4)
print_ll(merged)'''


#Recursive approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_sorted_lists(head1, head2):
    dummy = Node(0)

    current = dummy
    p1 = head1
    p2 = head2

 
def merge_recursive(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    if head1.data <= head2.data:
        head1.next = merge_recursive(head1.next, head2)
        return head1
    else:
        head2.next = merge_recursive(head1, head2.next)
        return head2

def print_ll1(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("None")

n1 = Node(3);
n2 = Node(5);
n3 = Node(7)

n1.next = n2
n2.next = n3

n4 = Node(9);
n5 = Node(11);
n6 = Node(12)

n4.next = n5
n5.next = n6

merged2 = merge_recursive(n1, n4)
print_ll1(merged2)