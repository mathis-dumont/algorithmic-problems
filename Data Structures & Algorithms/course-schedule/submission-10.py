class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            g[b].append(a)

        UNVISITED, VISITING, VISITED = 0, 1, 2

        states = [UNVISITED] * numCourses

        def dfs(c):
            if states[c] == VISITING:
                return False
            if states[c] == VISITED:
                return True
            states[c] = VISITING
            for nei in g[c]:
                if not dfs(nei):
                    return False
            states[c] = VISITED

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True