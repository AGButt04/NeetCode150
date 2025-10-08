class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return root

    left = root.left
    root.left = root.right
    root.right = left

    invertTree(root.left)
    invertTree(root.right)

    return root

def maxDepth(root):
    if not root:
        return 0

    leftTree = maxDepth(root.left) + 1
    rightTree = maxDepth(root.right) + 1

    return max(leftTree, rightTree)
