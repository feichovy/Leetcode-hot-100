# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
def buildTree(values):
    if not values:
        return None
    Nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = Nodes[::-1]
    root = kids.pop()
    for node in Nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    root1 = buildTree([])
    print(Solution().maxDepth(root1))  # Output: 0

    root2 = buildTree([3,9,20,None,None,15,7])
    print(Solution().maxDepth(root2))  # Output: 3

    root3 = buildTree([1,None,2, None, 3])
    print(Solution().maxDepth(root3))  # Output: 2