class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def add1toLL(head):
    def helper(node):
        if node is None:
            return 1  # base case: add 1 at the end (least significant digit)
        
        carry = helper(node.next)
        node.data += carry

        if node.data < 10:
            return 0  # no further carry needed
        else:
            node.data = 0
            return 1  # carry over to the previous node

    carry = helper(head)
    if carry == 1:
        newnode = Node(1)
        newnode.next = head
        return newnode
    return head
def printList(head):
    while head:
        print(head.data, end="")
        head = head.next
    print()

# Example: 9 -> 9 -> 9 becomes 1000
head = Node(9)
head.next = Node(9)
head.next.next = Node(9)

print("Original List:")
printList(head)

head = add1toLL(head)

print("After Adding 1:")
printList(head)

