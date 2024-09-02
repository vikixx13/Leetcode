class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=[]
        nmap={}
        for n in nums:
            if n in nmap:
                nmap[n]+=1
            else:
                nmap[n]=1
        
        for key, value in nmap.items():
            if value == 1:
                result.append(key)

        return result