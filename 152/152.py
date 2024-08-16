import numpy as np
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p = max(nums)
        cmax,cmin=1,1

        for n in nums:
            if n==0:
                cmax,cmin=1,1
                continue
            temp=cmax*n
            cmax=max(cmax*n,cmin*n,n)
            cmin=min(cmin*n,temp,n)
            p=max(cmax,p)
        return p