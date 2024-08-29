class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        candidate=-10e5
        for n in nums:
            if abs(n) < abs(candidate):
                candidate = n
            if abs(n) == abs(candidate):
                candidate = max(n, candidate)

        return candidate