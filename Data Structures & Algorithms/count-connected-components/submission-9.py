class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {i:[] for i in range(n)}

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        res = 0

        visit = set()

        if not edges:
            return 0

        def dfs(i):
            visit.add(i)
            for nei in g[i]:
                if nei not in visit:
                    dfs(nei)
            
        for i in range(n):
            if i not in visit:
                res +=1
                dfs(i)

        return res

        