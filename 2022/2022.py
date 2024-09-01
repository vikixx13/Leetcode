class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result=[[0] * n for _ in range(m)]
        if m*n != len(original):
            return []
        idx=0
        for i in range(m):
            for j in range(n):
                result[i][j]=original[idx]
                idx+=1
        
        return result