class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

def deletemiddlenode(head):
    if head == None or head.next == None:
        return None

    temp = head
    n = 0
    while temp != None:
        n += 1
        temp = temp.next

    res = n // 2  # Middle node position (0-based)

    # If deleting the head
    if res == 0:
        return head.next

    temp = head
    count = 0
    while temp != None:
        if count == res - 1:
            if temp.next:
                temp.next = temp.next.next  # Skip middle node
            break
        count += 1
        temp = temp.next

    return head
def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

# Create list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Before deletion:")
print_list(head)

head = deletemiddlenode(head)

print("After deletion:")
print_list(head)
