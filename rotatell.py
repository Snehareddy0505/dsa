class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def find_nth_node(head, n):
    """Helper function to find the nth node in the list."""
    curr = head
    count = 1
    while curr and count < n:
        curr = curr.next
        count += 1
    return curr


def rotate_ll(head, k):
    if not head or not head.next or k == 0:
        return head

    # Step 1: find length and last node
    tail = head
    length = 1
    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: handle cases where k >= length
    k = k % length
    if k == 0:
        return head

    # Step 3: find the new last node (length - k)th node
    new_last = find_nth_node(head, length - k)
    new_head = new_last.next

    # Step 4: rotate the list
    tail.next = head      # connect end to head
    new_last.next = None  # break the link

    return new_head


# --- Example usage ---
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original list:")
print_list(head)

rotated = rotate_ll(head, 2)
print("After rotating by 2:")
print_list(rotated)
