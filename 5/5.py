class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=[0,0]
        dp=[[False]*(n) for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = i,i+1

        for difference in range(2,n):
            for i in range(n-difference):
                j = i + difference
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = i,j
        i,j = ans     
        return s[i:j+1]

