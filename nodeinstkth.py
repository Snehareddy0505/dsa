class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def insert_at_kth_position(head, value, k):
    new_node = Node(value)

    # Case 1: Insert at head
    if k == 0:
        new_node.next = head
        return new_node

    current = head
    count = 0

    # Traverse to the (k - 1)th node
    while current is not None and count < k - 1:
        current = current.next
        count += 1

    # If k is greater than the length of the list
    if current is None:
        print(f"Position {k} is out of bounds.")
        return head

    # Insert the new node
    new_node.next = current.next
    current.next = new_node
    return head
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Create initial list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Original list:")
print_list(head)

# Insert 15 at position 1
head = insert_at_kth_position(head, 15, 1)

print("After inserting 15 at position 1:")
print_list(head) 

# Insert 5 at position 0 (head)
head = insert_at_kth_position(head, 5, 0)

print("After inserting 5 at position 0:")
print_list(head)

# Try inserting at a position out of bounds
head = insert_at_kth_position(head, 100, 10)  # Should print warning
 