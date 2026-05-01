class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            g[a].append(b)        
        
        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses

        def dfs(course):
            if states[course] == VISITING:
                return False
            if states[course] == VISITED:
                return True
            states[course] = VISITING

            for neighbor in g[course]:
                if not dfs(neighbor):
                    return False
            states[course] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True     