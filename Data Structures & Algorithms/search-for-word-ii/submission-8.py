class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        res = set()

        rows, cols = len(board), len(board[0])

        root = Node()
        for word in words:
            root.addWord(word)

        def dfs(r,c,node,word):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] not in node.children:
                return 
            else:
                word+=board[r][c]
                node = node.children[board[r][c]]
                if node.is_end:
                    res.add(word)
                
                tmp = board[r][c]
                board[r][c] = '#'

                dfs(r-1,c,node,word)
                dfs(r+1,c,node,word)
                dfs(r,c-1,node,word)
                dfs(r,c+1,node,word)
                board[r][c] = tmp

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,"")
        
        return list(res)