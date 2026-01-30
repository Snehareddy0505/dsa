class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

# Function to calculate length of the linked list
def length(head):
    count = 0
    temp = head
    while temp is not None:
        count += 1
        temp = temp.next
    return count
# Creating linked list: 10 -> 20 -> 30
node3 = Node(30)
node2 = Node(20, node3)
node1 = Node(10, node2)

# Calculate and print length
print("Length of linked list:", length(node1))
