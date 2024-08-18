class Solution:
    def nthUglyNumber(self, n: int) -> int:
        multi = [2,3,5]
        uheap = [1]
        visited = set()
        visited.add(1)
        for _ in range(n):
            c = heappop(uheap)
            for m in multi:
                new_u = c * m
                if new_u not in visited:
                    heappush(uheap, new_u)
                    visited.add(new_u)
        return c
            