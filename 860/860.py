class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=0
        t=0
        ty=0
        for i in range(len(bills)):
            if bills[i]==5:
                f+=1
            if bills[i]==10:
                t+=1
                if f==0:
                    return False
                else:
                    f-=1
            if bills[i]==20:
                ty+=1
                if f>=1 and t>=1:
                    f-=1
                    t-=1
                elif f>=3 and t==0:
                    f-=3
                else:
                    return False
        
        return True