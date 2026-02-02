class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Helper function to reverse a linked list
def reverse(head):
    temp = head
    prev = None
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev


# Main function to check if linked list is a palindrome
def llispalindrome(head):
    if head is None or head.next is None:
        return True

    # Step 1: Find the middle of the list
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    second_half = reverse(slow.next)

    # Save the head of reversed part to restore later
    reverse_head = second_half

    # Step 3: Compare the first and second halves
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            reverse(reverse_head)  # Restore original list
            return False
        first_half = first_half.next
        second_half = second_half.next

    # Step 4: Restore the list and return True
    reverse(reverse_head)
    return True
# Helper to create a linked list
def create_linked_list(values):
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Example test
head = create_linked_list([1, 2, 3, 2, 1])
print(llispalindrome(head))  # Output: True

 