# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode], level = 0, res = None) -> List[List[int]]:

        if not root:
            return []
        if res is None:
            res = {}
        
        if level in res:
            res[level].append(root.val)
        else:
            res[level] = [root.val]

        level +=1

        self.levelOrder(root.left,level,res)
        self.levelOrder(root.right,level,res)

        if level ==1:
            output = []
            for l in res.values():
                output.append(l) 
            return output       

        