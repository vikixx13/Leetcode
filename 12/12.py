class Solution:
    def intToRoman(self, num: int) -> str:
        rmap={ 1:"I", 4:"IV", 5:"V", 9:"IX" , 10:"X" , 40:"XL", 50:"L" ,90: "XC", 100:"C", 400:"CD", 500:"D" , 900:"CM", 1000:"M"}
        e=10
        th=num//pow(e,3)
        h=(num%pow(e,3))//pow(e,2)
        t=(num%pow(e,2))//pow(e,1)
        o=(num%pow(e,1))//pow(e,0)
        s=""
        print(th,h,t,o)
        for _ in range(th):
            s+=rmap[1000]
        if h==9:
            s+=rmap[900]
        if h<4:
            for _ in range(h):
                s+=rmap[1]
        if h>=5 and h<9:
            s+=rmap[500]
            for _ in range(h-5):
                s+=rmap[100]
        if h==4:
            s+=rmap[400]
            
        if t<4:
            for _ in range(t):
                s+=rmap[10]
        if t>=5 and t<9:
            s+=rmap[50]
            for _ in range(t-5):
                s+=rmap[10]
        if t==9:
            s+=rmap[90]
        if t==4:
            s+=rmap[40]

        if o==4:
            s+=rmap[4]
        if o==9:
            s+=rmap[9]
        if o<4:
            for _ in range(o):
                s+=rmap[1]
        if o>=5 and o<9:
            s+=rmap[5]
            for _ in range(o-5):
                s+=rmap[1]
        return s