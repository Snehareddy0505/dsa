class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

def arrayToDoublyLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    temp = head
    for val in arr[1:]:
        newNode = Node(val)
        temp.next = newNode
        newNode.prev = temp
        temp = newNode
    return head
  
def printDLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def deleteHead(head):
    if head is None:
        return None
    new_head = head.next
    if new_head:
        new_head.prev = None
    del head
    return new_head

# Example usage
arr = [10, 20, 30, 40]
head = arrayToDoublyLinkedList(arr)

print("Original DLL:")
printDLL(head)

head = deleteHead(head)

print("After deleting head:")
printDLL(head)
