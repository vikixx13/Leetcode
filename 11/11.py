class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        a=0
        while l<r:            
            a=max(a,(min(height[l],height[r])) * (r-l))
            if height[r]>height[l]:
                l+=1
            else:
                r-=1
            print(a)
        return a