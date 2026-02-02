class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def delete_by_value(head, value):
    # If the list is empty
    if head is None:
        return None

    # If the head node is the one to delete
    if head.data == value:
        return head.next

    # Traverse to find the node just before the one to delete
    current = head
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next  # Skip the node to delete
            return head
        current = current.next

    # If the value is not found, return the original list
    return head
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Create linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

print("Original list:")
print_list(head)

# Delete the node with value 30
head = delete_by_value(head, 30)

print("After deleting value 30:")
print_list(head)
   