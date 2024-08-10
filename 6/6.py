class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        r=0
        d=1
        rows=[[] for _ in range (numRows)]
        
        for c in s:
            rows[r].append(c)
            if r==0:
                d=1
            elif r==numRows-1:
                d=-1
            r+=d

        for i in range(numRows):
            rows[i]=''.join(rows[i]) 

        return ''.join(rows)          