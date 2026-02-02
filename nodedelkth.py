class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def delete_kth_node(head, k):
    # If the list is empty or k is invalid
    if head is None or k <= 0:
        return head

    # If k == 1, delete the head
    if k == 1:
        return head.next

    # Traverse to the (k-1)th node
    current = head
    count = 1
    while current is not None and count < k - 1:
        current = current.next
        count += 1

    # If k is more than the number of nodes
    if current is None or current.next is None:
        return head

    # Delete the k-th node
    current.next = current.next.next
    return head
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list:")
print_list(head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Delete the 3rd node (value 3)
head = delete_kth_node(head, 3)

print("After deleting 3rd node:")
print_list(head)  # Output: 1 -> 2 -> 4 -> 5 -> 