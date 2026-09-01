class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {time[0]: [] for time in times}
        for time in times:
            graph[time[0]].append((time[2],time[1]))

        pq = [(0,k)]

        dist = {i:float('inf') for i in range(1,n+1)}
        dist[k]=0
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for weight,child in graph.get(node,[]):
                new_dist = weight + d
                if new_dist < dist[child]:
                    dist[child] = new_dist
                    heapq.heappush(pq,(new_dist,child))

        max_dist = max(dist.values())
        return max_dist if max_dist < float('inf') else -1
