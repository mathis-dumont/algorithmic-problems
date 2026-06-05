class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = {i:[] for i in range(numCourses)}
        in_order = [0] * numCourses

        res = []

        for a,b in prerequisites:
            g[b].append(a)
            in_order[a] +=1

        q = collections.deque([i for i in range(numCourses) if in_order[i]==0])

        while q:
            cur = q.popleft()
            res.append(cur)

            for nei in g[cur]:
                in_order[nei] -=1
                if in_order[nei]==0:
                    q.append(nei)
        
        return res if len(res) == numCourses else []