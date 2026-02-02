class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def insert_before_value(head, value_to_insert, target_value):
    new_node = Node(value_to_insert)

    # Case 1: Empty list
    if head is None:
        print("List is empty.")
        return head

    # Case 2: Inserting before the head
    if head.data == target_value:
        new_node.next = head
        return new_node

    # Traverse to find the node before the target
    current = head
    while current.next is not None and current.next.data != target_value:
        current = current.next

    # If target value not found
    if current.next is None:
        print(f"Value {target_value} not found in the list.")
        return head

    # Insert new node before the target node
    new_node.next = current.next
    current.next = new_node
    return head
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Create initial list: 10 -> 20 -> 30 -> 40
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original list:")
print_list(head)

# Insert 25 before 30
head = insert_before_value(head, 25, 30)

print("After inserting 25 before 30:")
print_list(head)

 