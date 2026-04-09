# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            maxLeft = max(0, dfs(node.left))
            maxRight = max(0, dfs(node.right))

            res[0] = max(res[0], maxLeft + node.val + maxRight)

            return max(node.val + maxLeft, node.val + maxRight)
        
        dfs(root)
        return res[0]