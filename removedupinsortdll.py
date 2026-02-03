class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


def removeDupInSortedDLL(head):
    temp = head
    while temp is not None and temp.next is not None:
        nextnode = temp.next
        while nextnode is not None and nextnode.data == temp.data:
            nextnode = nextnode.next
        temp.next = nextnode
        if nextnode is not None:
            nextnode.prev = temp
        temp = temp.next
    return head
# Helper to print DLL
def printDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" <-> " if curr.next else "\n")
        curr = curr.next

# Create sorted DLL: 1 <-> 2 <-> 2 <-> 3 <-> 3 <-> 4
head = Node(1)
head.next = Node(2); head.next.prev = head
head.next.next = Node(2); head.next.next.prev = head.next
head.next.next.next = Node(3); head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(3); head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(4); head.next.next.next.next.next.prev = head.next.next.next.next

print("Before:")
printDLL(head)

head = removeDupInSortedDLL(head)

print("After removing duplicates:")
printDLL(head)

