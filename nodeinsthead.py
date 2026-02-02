class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def insert_at_head(head, value):
    new_node = Node(value)
    new_node.next = head
    return new_node
# Helper function to print the list
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Initial list: 20 -> 30
head = Node(20)
head.next = Node(30)

print("Original list:")
print_list(head)

# Insert 10 at head
head = insert_at_head(head, 10)

print("After inserting 10 at head:")
print_list(head)
