class NodeTrie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def addWord(self,word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = NodeTrie()
            cur = cur.children[c]
        cur.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []

        res = set()
        root = NodeTrie()
        rows, cols = len(board), len(board[0])

        for word in words:
            root.addWord(word)
        
        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children:
                return
            else:
                # board[r][c] in node.children
                word += board[r][c]
                child = node.children[board[r][c]]

                if child.is_end:
                    res.add(word)
                    child.is_end = False
                
                # backtracking
                tmp = board[r][c]
                board[r][c] = '#'

                dfs(r-1,c,child,word)
                dfs(r+1,c,child,word)
                dfs(r,c-1,child,word)
                dfs(r,c+1,child,word)

                board[r][c] = tmp

                # reducing the tree dynamically:
                if not child.children:
                    del node.children[tmp]
                return

        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,"")

        return list(res)