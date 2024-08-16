class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn=arrays[0][0]
        mx=arrays[0][-1]
        d=0
        for i in range(1,len(arrays)):            
            d=max(d,abs(mx-arrays[i][0]),abs(arrays[i][-1]-mn))
            mn=min(mn,arrays[i][0])
            mx=max(mx,arrays[i][-1])
        
        return d