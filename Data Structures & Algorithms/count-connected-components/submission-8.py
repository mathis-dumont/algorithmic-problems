class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = {i:[] for i in range(n)}
        visit = set()
        cnt = 0

        for n1,n2 in edges:
            g[n1].append(n2)
            g[n2].append(n1)

        def dfs(node):
            visit.add(node)
            for neighbor in g[node]:
                if neighbor not in visit:
                    dfs(neighbor)
        for i in range(n):
            if i not in visit:
                cnt +=1
                dfs(i)

        return cnt