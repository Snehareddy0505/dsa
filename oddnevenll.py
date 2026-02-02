class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def oddeven(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
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
#head.next.next.next = Node(4)
#head.next.next.next.next = Node(5)

print("Original List:")
print_list(head)

head = oddeven(head)

print("Reordered List (Odd positions first):")
print_list(head)
