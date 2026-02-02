class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def insert_at_tail(head, value):
    new_node = Node(value)
    
    # If the list is empty, the new node becomes the head
    if head is None:
        return new_node

    # Traverse to the last node
    current = head
    while current.next is not None:
        current = current.next

    # Insert new node at the end
    current.next = new_node
    return head
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Initial list: 10 -> 20
head = Node(10)
head.next = Node(20)

print("Original list:")
print_list(head)

# Insert 30 at tail (before None)
head = insert_at_tail(head, 50  )

print("After inserting 30 before None (at tail):")
print_list(head)
