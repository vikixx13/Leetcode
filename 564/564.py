class Solution:
    def gen_palin(self, l: int, even: bool) -> int:
        x=l
        if not even:
            l = l//10
        while l > 0:
            x = x * 10 + l % 10
            l//=10
        return x
    def nearestPalindromic(self, n: str) -> str:
        l=len(n)
        mid=l // 2-1 if l % 2 == 0 else l // 2
        fhalf=int(n[:mid+1])
        pal=[]
        pal.append(self.gen_palin(fhalf,l % 2 == 0))
        pal.append(self.gen_palin(fhalf-1,l % 2 == 0))
        pal.append(self.gen_palin(fhalf+1,l % 2 == 0))
        pal.append(10**(l-1)-1)
        pal.append(10**l+1)

        dif=float("inf")
        palin=0
        nn=int(n)
        for p in pal:
            if p==nn:
                continue
            if abs(p-nn)<dif:
                palin=p
                dif=abs(p-nn)
            elif abs(p-nn)==dif:
                palin=min(p,palin)
        return str(palin)