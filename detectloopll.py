class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
def detectloop(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Build sample list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next  # 6 -> 3

# Detect loop
has_loop = detectloop(head)
print(has_loop)  # Output: True

