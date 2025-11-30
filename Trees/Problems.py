from collections import deque

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

def diameterOfBinaryTree(root):
    dia = 0

    def DFS(root):
        nonlocal dia
        if not root:
            return 0

        left = DFS(root.left)
        right = DFS(root.right)
        dia = max(dia, left + right)

        return max(left, right) + 1

    DFS(root)
    return dia

def isBalanced(root):
    def DFS(root):
        if not root:
            return [True, 0]

        left = DFS(root.left)
        right = DFS(root.right)

        balanced = left[0] and right[0] and abs(right[1] - left[1]) <= 1

        return [balanced, max(left[1], right[1]) + 1]

    return DFS(root)[0]

def isSameTree(p, q):
    if not p and not q:
        return True

    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

def levelOrder(self, root):
    if not root:
        return []

    queue = deque()
    traversal = []
    queue.append(root)

    while queue:
        n = len(queue)
        level = []

        for i in range(n):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        traversal.append(level)

    return traversal

def isSubtree(self, root, subRoot):
    if not root:
        return False

    if self.sameTree(root, subRoot):
        return True

    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

def sameTree(self, root, subroot):
    if not root and not subroot:
        return True
    if not root or not subroot:
        return False
    if root.val != subroot.val:
        return False

    left = self.sameTree(root.left, subroot.left)
    right = self.sameTree(root.right, subroot.right)

    return left and right
