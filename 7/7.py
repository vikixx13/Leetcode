class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        n=str(abs(x))
        n=n[::-1]
        x=int(n)
        x=-x if neg else x
        if x < -2**31 or x > 2**31 - 1:
            return(0)
        else:
            return(x)