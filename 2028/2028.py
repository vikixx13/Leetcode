class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        msum=sum(rolls)
        nsum = ((m + n) * mean) - msum
        if nsum > 6*n or nsum <n:
            return []
        temp = nsum//n
        left = nsum % n
        miss = [temp] * n
        for i in range(left):
            miss[i]+=1

        return miss

