class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def reversell(head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev

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

print("Original List:")
printList(head)

# Reverse the list
head = reversell(head)

print("Reversed List:")
printList(head)
