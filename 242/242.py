from collections import Counter
#brute force
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                t=t.replace(c,"",1)
                continue
            else:
                return False
        if len(t)>0:
            return False
        return True
    
#counter method
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)