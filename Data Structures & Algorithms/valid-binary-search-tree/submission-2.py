# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))
    def valid(self, node, inf, sup):
        if not node:
            return True
        if not (node.val < sup and node.val > inf):
            return False
        
        return (self.valid(node.left, inf, node.val) and
        self.valid(node.right, node.val, sup))
        