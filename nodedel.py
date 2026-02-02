class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def delete(head):
    if head is None:
        return None
    return head.next
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original list:")
print_list(head) 

# Delete head
head = delete(head)

print("After deleting head:")
print_list(head)
