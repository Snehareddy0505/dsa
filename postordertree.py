class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")
root=TreeNode(1,TreeNode(2),TreeNode(3))
postorder(root)