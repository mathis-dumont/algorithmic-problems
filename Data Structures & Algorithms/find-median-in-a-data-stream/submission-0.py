class MedianFinder:

    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))

        if len(self.hi) > len(self.lo) + 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if not self.lo and not self.hi:
            return
        elif len(self.lo) != len(self.hi):
            return self.hi[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2.0
        
        