class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        g = {i:[] for i in range(n)}
        visit = set()

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(node):
            visit.add(node)
            for nei in g[node]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                res+=1
                dfs(i)

        return res