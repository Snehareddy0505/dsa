class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)
root=TreeNode(1,TreeNode(2),TreeNode(3))
inorder(root)