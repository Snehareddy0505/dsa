class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def intersectionPointLL(head1, head2):
    if head1 is None or head2 is None:
        return None

    t1 = head1
    t2 = head2

    while t1 != t2:
        t1 = t1.next if t1 else head2
        t2 = t2.next if t2 else head1

    return t1  # Can be None if there's no intersection
# Shared part
common = Node(8)
common.next = Node(10)

# List A
head1 = Node(1)
head1.next = Node(2)
head1.next.next = common

# List B
head2 = Node(3)
head2.next = common

# Run intersection finder
result = intersectionPointLL(head1, head2)
if result:
    print("Intersection at node with value:", result.data)
else:
    print("No intersection")

