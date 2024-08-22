class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num).replace("0b", "")
        l=len(b)
        b=int(b,2)
        compliment = b ^ ((2**l) - 1)
        return compliment
