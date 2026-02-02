class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None 

def findTail(head):
    curr = head
    while curr.next:
        curr = curr.next
    return curr


def pairsWithSumInDLL(head, target_sum):
    left = head
    right = findTail(head)
    result = []

    while left != right and right.next != left:
        current_sum = left.data + right.data
        if current_sum == target_sum:
            result.append((left.data, right.data))
            left = left.next
            right = right.prev
        elif current_sum < target_sum:
            left = left.next
        else:
            right = right.prev

    return result
# Construct DLL: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
head = Node(1)
head.next = Node(2); head.next.prev = head
head.next.next = Node(3); head.next.next.prev = head.next
head.next.next.next = Node(4); head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5); head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(6); head.next.next.next.next.next.prev = head.next.next.next.next

pairs = pairsWithSumInDLL(head, 7)
print(pairs)
