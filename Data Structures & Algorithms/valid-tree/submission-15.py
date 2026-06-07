class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = {i:[] for i in range(n)}
        visit = set()

        if len(edges) != n-1:
            return False

        for a,b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(i,prev):
            if i in visit:
                return False

            visit.add(i)
            for nei in g[i]:
                if nei != prev:
                    if not dfs(nei,i):
                        return False
            return True

        return dfs(0,-1) and len(visit) == n

        
