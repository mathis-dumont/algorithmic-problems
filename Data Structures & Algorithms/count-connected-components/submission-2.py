class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        count = 0
        visit = set()

        g = {i:[] for i in range(n)}

        for n1,n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        def dfs(i):
            if i in visit:
                return 
            visit.add(i)
            for neighbor in g[i]:
                dfs(neighbor)

        for i in range(n):
            if i not in visit:
                count+=1
                dfs(i)

        return count