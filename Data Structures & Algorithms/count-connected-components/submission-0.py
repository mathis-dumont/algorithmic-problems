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

        def dfs(i, prev):
            if i in visit:
                return False
            visit.add(i)

            for neighbor in g[i]:
                if prev != neighbor:
                    dfs(neighbor,i)
            return True

        for i in range(n):
            if dfs(i,-1):
                count+=1

        return count