#O(mn)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(haystack)
        n=len(needle)
        i=0
        while i<m-n:
            r=i
            l=1
            if needle[0]==haystack[i]:
                idx=i
                while l<n:
                    if needle[l]==haystack[r]:
                        r+=1
                    else:
                        idx=-1
        return idx


#O(m+n)
