class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def removenthnodeend(head, n):
    dummy = Node(0)  # dummy node to handle edge cases (e.g. deleting head)
    dummy.next = head
    fast = slow = dummy

    # Move fast pointer n+1 steps ahead to maintain a gap
    for _ in range(n + 1):
        if fast:
            fast = fast.next
        else:
            return head  # n is larger than the length of the list

    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the nth node from end
    to_delete = slow.next
    slow.next = slow.next.next
    del to_delete

    return dummy.next
# Helper to print list
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

# Remove 2nd node from end (should remove 4)
head = removenthnodeend(head, 2)
printList(head)  # Output: 1 -> 2 -> 3 -> 5 -> None
