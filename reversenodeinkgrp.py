class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def findKthNode(temp, k):
    count = 1
    while temp is not None and count < k:
        temp = temp.next
        count += 1
    return temp


def reverseSegment(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev  # new head after reversal


def reverseNodeInKGroup(head, k):
    temp = head
    prevLast = None
    newHead = None

    while temp is not None:
        kthNode = findKthNode(temp, k)
        if kthNode is None:
            if prevLast:
                prevLast.next = temp
            break

        nextNode = kthNode.next
        kthNode.next = None

        # reverse the current group
        reversedHead = reverseSegment(temp)

        # connect previous group
        if newHead is None:
            newHead = reversedHead
        else:
            prevLast.next = reversedHead

        prevLast = temp
        temp = nextNode

    return newHead if newHead else head
# Helper to print the list
def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

print("Original list:")
printList(head)

k = 3
head = reverseNodeInKGroup(head, k)

print(f"\nList after reversing in groups of {k}:")
printList(head)


