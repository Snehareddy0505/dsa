class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # Important: return new head after reversing

def add1toLL(head):
    head = reverse(head)  # Step 1: Reverse the list
    temp = head
    carry = 1             # Step 2: Initialize carry as 1 (for adding 1)

    prev = None
    while temp is not None:
        temp.data += carry
        if temp.data < 10:
            carry = 0
            break
        else:
            temp.data = 0
            carry = 1
        prev = temp
        temp = temp.next

    # If carry is still left, add a new node
    if carry == 1:
        prev.next = Node(1)

    head = reverse(head)  # Step 3: Reverse back
    return head
def printList(head):
    while head:
        print(head.data, end="")
        head = head.next
    print()

# Example: 1 -> 9 -> 9 => 200
head = Node(1)
head.next = Node(9)
head.next.next = Node(9)

print("Original List:")
printList(head)

head = add1toLL(head)

print("After Adding 1:")
printList(head)
