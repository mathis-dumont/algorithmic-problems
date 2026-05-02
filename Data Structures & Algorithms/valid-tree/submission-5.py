class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        g = {i:[] for i in range(n)}

        for n1,n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        visit = set()
        def dfs(node, prev):
            visit.add(node)
            for neighbor in g[node]:
                if neighbor == prev:
                    continue
                if neighbor in visit:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0,-1) and len(visit) == n


            
        