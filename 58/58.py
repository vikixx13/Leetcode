import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=re.findall('\S+',s)
        last=words.pop()
        return len(last)