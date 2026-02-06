class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createdLL(arr):
    head=None
    for val in arr:
        if head==None:
            head=Node(val)
            temp=head
        else:
           newNode=Node(val)
           newNode.prev=temp
           temp.next=newNode
           temp=temp.next
    return head.data
arr=[1,2,3]
print(createdLL(arr))