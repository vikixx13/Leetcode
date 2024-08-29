class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=len(word1)
        m=len(word2)
        j=1
        result=""
        for i in range(max(n,m)):
            if i<n and i<m:
                result=result+word1[i]+word2[i]
            else:
                if i>=n:
                    result=result+word2[i]
                elif i>=m:
                    result=result+word1[i]
        
        return result

