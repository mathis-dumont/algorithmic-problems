class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {i: [] for i in range(numCourses)}
        order = []

        in_degree = [0] * numCourses
        for a,b in prerequisites:
            g[b].append(a)
            in_degree[a] += 1

        q = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])

        while q:
            c = q.popleft()
            order.append(c)
            for following_course in g[c]:
                in_degree[following_course] -= 1
                if in_degree[following_course] == 0:
                    q.append(following_course)
        
        return order if len(order) == numCourses else []
