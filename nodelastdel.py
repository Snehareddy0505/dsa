class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def delete_last_node(head):
    # If the list is empty
    if head is None:
        return None

    # If the list has only one node
    if head.next is None:
        return None

    # Traverse the list to find the second last node
    temp = head
    while temp.next.next is not None:
        temp = temp.next

    # Remove the last node
    temp.next = None
    return head
# Helper function to print the list
def print_list(head):
    while head:    
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Create the linked list: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original list:")
print_list(head)  # Output: 1 -> 2 -> 3 -> None

# Delete the last node
head = delete_last_node(head)

print("After deleting last node:")
print_list(head)  # Output: 1 -> 2 -> None
