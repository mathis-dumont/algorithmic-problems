class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {i:[] for i in range(numCourses)}

        for a,b in prerequisites:
            g[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        courses = [UNVISITED] * numCourses

        def dfs(i):
            if courses[i] == VISITING:
                return False
            if courses[i] == VISITED:
                return True
            courses[i] = VISITING
            for prer in g[i]:
                if not dfs(prer):
                    return False

            courses[i] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True