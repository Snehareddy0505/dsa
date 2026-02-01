class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

def reverse_dll(head):
    if head is None or head.next is None:
        return head

    current = head
    while current is not None:
        current.prev, current.next = current.next, current.prev
        head = current
        current = current.prev

    return head

# Helper function to print the list from head to tail
def print_dll(head):
    current = head
    while current:
        print(current.data, end=" <-> " if current.next else "\n")
        current = current.next

# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Link nodes (1 <-> 2 <-> 3 <-> 4)
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

# Head of the original DLL
head = node1

print("Original DLL:")
print_dll(head)

# Reverse the DLL
head = reverse_dll(head)

print("Reversed DLL:")
print_dll(head)
