# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root :
            return 0

        depth = 1
        depth_left = 0
        depth_right = 0
        
        if root.left:
            depth_left = self.maxDepth(root.left)

        if root.right:
            depth_right = self.maxDepth(root.right)
        
        depth += max(depth_right,depth_left)


        return depth        
        