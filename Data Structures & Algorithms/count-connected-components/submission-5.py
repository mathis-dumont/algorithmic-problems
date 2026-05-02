class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        g = {i:[] for i in range(n)}

        for n1,n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for neighbor in g[node]:
                dfs(neighbor)
            return True
            
        for i in range(n):
            if dfs(i):
                count +=1
        
        return count
                