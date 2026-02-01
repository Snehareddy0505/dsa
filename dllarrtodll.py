# Define a Node for the Doubly Linked List
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

# Function to convert array to doubly linked list
def arrayToDoublyLinkedList(arr):
    if not arr:  # If the array is empty
        return None

    # Create the head node
    head = Node(arr[0])
    temp = head

    # Loop through the remaining elements
    for val in arr[1:]:
        newNode = Node(val)
        temp.next = newNode  # Link current node to new node
        newNode.prev = temp  # Link new node back to current node
        temp = newNode       # Move temp to new node

    return head  # Return the head of the created DLL

# Function to print the DLL (forward direction)
def printDLL(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()

# Example usage:
arr = [10, 20, 30, 40, 50]
head = arrayToDoublyLinkedList(arr)

print("Doubly Linked List from array:")
printDLL(head)
