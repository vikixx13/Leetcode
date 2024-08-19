#recursion
class Solution:
    def rec(self, curl: int, pastel: int) -> int:
        if curl == self.n:
            return 0
        if curl > self.n:
            return 1000
        o1 = 2 + self.rec(curl * 2, curl)
        o2 = 1 + self.rec(curl + pastel, pastel)
        return min(o1,o2)
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        self.n=n
        return 1 + self.rec(1,1)

        
