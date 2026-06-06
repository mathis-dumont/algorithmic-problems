class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        g = {i:[] for i in range(n)}
        visit = set()

        for e1,e2 in edges:
            g[e1].append(e2)
            g[e2].append(e1)

        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            
            for children in g[i]:
                if children != prev:
                    if not dfs(children,i):
                        return False

            return True
        
        return dfs(0,-1) and len(visit) == n
