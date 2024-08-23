import re
class Solution:
    def fractionAddition(self, expression: str) -> str:
        num=0
        dnom=1

        nums=re.split("/|(?=[-+])",expression)
        nums=list(filter(None,nums))

        for i in range(0,len(nums),2):
            cnum = int(nums[i])
            cdnom = int(nums[i+1])

            num = num*cdnom + dnom*cnum
            dnom = dnom*cdnom
        gcd = abs(self.GCD(num,dnom))

        num//=gcd
        dnom//=gcd

        return str(num)+"/"+str(dnom)

    def GCD(self, a: int,b :int):
        if a==0:
            return b
        return self.GCD(b%a,a)
        