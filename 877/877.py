from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #return True
        n=len(piles)

        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            turn = (j - i - n) % 2
            if turn == 1:  
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, n - 1) > 0
