class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l=0
        r=num
        while l<=r:
            mid = (l+r) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r = mid -1
            else:
                l = mid + 1

        return False