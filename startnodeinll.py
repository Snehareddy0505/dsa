
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def startingnode(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Cycle detected, find the start
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next  # ✅ both move one step
            return slow  # ✅ return start of loop

    return None  # ✅ No cycle
# Helper to create a cycle
def create_cycle():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = third  # Cycle starts at node with value 3

    return head

head = create_cycle()
start = startingnode(head)
if start:
    print("Cycle starts at node with value:", start.data)
else:
    print("No cycle detected.")

