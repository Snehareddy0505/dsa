class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None  # Needed for doubly linked list

def delete_all_occur_of_key_dll(head, key):
    temp = head
    while temp is not None:
        if temp.data == key:
            # Save next node before deletion
            next_node = temp.next

            # If temp is head
            if temp == head:
                head = next_node
                if head:
                    head.prev = None
            else:
                # Remove temp from the list
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev

            temp = next_node  # Move to next node after deletion
        else:
            temp = temp.next

    return head
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> " if temp.next else "\n")
        temp = temp.next

# Create doubly linked list: 1 <-> 2 <-> 3 <-> 2 <-> 4
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(2)
fifth = Node(4)

head.next = second
second.prev = head
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

print("Before deletion:")
print_list(head)

# Delete all occurrences of 2
head = delete_all_occur_of_key_dll(head, 2)

print("After deletion:")
print_list(head)

