class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b=bin(n).replace("0b", "")
        l=len(b)
        b=int(b,2)
        compliment = b ^ ((2**l) - 1)
        return compliment
