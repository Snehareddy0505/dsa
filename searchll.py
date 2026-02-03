class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Function to search for a value in the linked list
def search(head, key):
    temp = head
    while temp is not None:
        if temp.data == key:
            return True  # Found the key
        temp = temp.next
    return False  # Key not found
# Create linked list: 5 -> 15 -> 25
node3 = Node(25)
node2 = Node(15, node3)
node1 = Node(5, node2)

# Search for values
print("Is 15 in the list?", search(node1, 15))  # True
print("Is 30 in the list?", search(node1, 30))  # False
