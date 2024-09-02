# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        r=n
        while l<r:
            mid=(r+l)//2
            if isBadVersion(mid):
                r=mid
            elif not isBadVersion(mid):
                l=mid + 1
        return r