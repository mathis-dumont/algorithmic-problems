class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        g = {i:[] for i in range(n)}

        for n1,n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        visit = set()

        def dfs(i):
            visit.add(i)
            for neighbor in g[i]:
                if neighbor not in visit:
                    dfs(neighbor)
            return

        for i in range(n):
            if i not in visit:
                cnt +=1
                dfs(i)

        return cnt