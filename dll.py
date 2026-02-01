class Node:
    def __init__(self, val):
        self.prev = None
        self.data = val
        self.next = None

def createDLL(arr): 
    head = None
    temp = None
    for val in arr:
        newNode = Node(val)
        if head is None:
            head = newNode
            temp = head
        else:
            temp.next = newNode
            newNode.prev = temp
            temp = newNode
    return head  # Return the head of the DLL

def printDLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()  # For newline

# Test the DLL creation
arr = [1, 2, 3, 4, 5]
head = createDLL(arr)
print("Doubly Linked List (Forward):")
printDLL(head)

