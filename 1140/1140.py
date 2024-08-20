class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n=len(piles)
        m=1
        dp=[[0] * (n+1) for _ in range(n+1)]
        ss=[0 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            ss[i]=ss[i+1]+piles[i]
        
        for i in range(n+1):
            dp[i][n] = ss[i]

        for i in range(n-1,-1,-1):
            for j in range(n-1,0,-1):
                for X in range(1, min(2 * j, n - i) + 1):
                    dp[i][j] = max(dp[i][j],ss[i] - dp[i + X][max(j, X)],)

        return dp[0][m]
