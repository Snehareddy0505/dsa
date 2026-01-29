class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(-1)
    curr = dummy
    carry = 0

    while l1 or l2:
        sum = carry
        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next

    if carry:
        curr.next = ListNode(carry)

    return dummy.next

# -----------------------------
# 🔧 Helper functions for testing
# -----------------------------

def build_linked_list(nums):
    """Builds a linked list from a list of numbers and returns the head."""
    dummy = ListNode(-1)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Prints the linked list in a readable format."""
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# -----------------------------
# ✅ Example usage
# -----------------------------

# Example 1: (342 + 465 = 807)
l1 = build_linked_list([2, 4, 3])  # represents 342
l2 = build_linked_list([5, 6, 4])  # represents 465

result = addTwoNumbers(l1, l2)

print("Result:")
print_linked_list(result)  # Expected: 7 -> 0 -> 8

