class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string=""
        for c in s:
            string+=str(ord(c) - ord("a") + 1)
        
        while k>0:
            dsum=0
            for d in string:
                dsum += int(d)
            string = str(dsum)
            k-=1
        
        return dsum