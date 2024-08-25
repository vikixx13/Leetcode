class Solution:
    def isValid(self, word: str) -> bool:
        vow='aeiou'
        vowels=vow + vow.upper()
        con='bcdfghjklmnpqrstvwxyz'
        consts=con + con.upper()
        
        if len(word) < 3:
            return False
        c=False
        v=False
        for char in word:
            if not(char.isalnum()):
                return False
            if char in vowels:
                v=True
            if char in consts:
                c=True
        return c and v