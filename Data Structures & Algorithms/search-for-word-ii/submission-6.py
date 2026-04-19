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
        root = NodeTrie()
        res = set()

        for word in words:
            root.addWord(word)
        
        rows, cols = len(board), len(board[0])

        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] not in node.children:
                return
            else:
                word += board[r][c]
                node = node.children[board[r][c]]
                if node.is_end:
                    res.add(word)

                # backtracking
                tmp = board[r][c] 
                board[r][c] = '#'

                dfs(r+1,c,node,word)
                dfs(r-1,c,node,word)
                dfs(r,c+1,node,word)
                dfs(r,c-1,node,word)

                board[r][c] = tmp
                        
        for i in range(rows):
            for j in range(cols):
                dfs(i,j,root,"")

        return list(res)