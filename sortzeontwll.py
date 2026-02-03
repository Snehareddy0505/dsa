class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def sortzeroonetwo(head):
    if head is None or head.next is None:
        return head

    # Dummy nodes to hold the starting points of 0s, 1s, and 2s lists
    zerohead = Node(-1)
    onehead = Node(-1)
    twohead = Node(-1)

    # Tail pointers for 0s, 1s, and 2s
    zero = zerohead
    one = onehead
    two = twohead

    # Traverse the original list and assign nodes to the corresponding lists
    temp = head
    while temp is not None:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next
        elif temp.data == 1:
            one.next = temp
            one = one.next
        else:
            two.next = temp
            two = two.next
        temp = temp.next

    # Connect the three lists
    # If there's at least one node in 1s list
    zero.next = onehead.next if onehead.next else twohead.next
    one.next = twohead.next
    two.next = None

    # Head of the sorted list
    return zerohead.next
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(0)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)

print("Original list:")
printList(head)

sorted_head = sortzeroonetwo(head)

print("Sorted list:")
printList(sorted_head)
