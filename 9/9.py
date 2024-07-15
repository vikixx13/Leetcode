class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        n=x[::-1]
        if x==n:
            return True
        else:
            return False   