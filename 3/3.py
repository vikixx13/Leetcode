class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smap={}
        maxlen=0
        l=0
        for r in range(len(s)):
            if s[r] not in smap or smap[s[r]]<l:
                smap[s[r]]=r
                maxlen=max(maxlen,r-l+1)
            else:
                l=smap[s[r]] + 1
                smap[s[r]]=r 
        return maxlen