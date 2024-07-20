class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        p=n-1
        num=0
        for i in range(n):
            temp=digits[i]*(pow(10,p))
            p-=1
            num=temp+num
        num+=1
        output = list(map(int, str(num)))   
        return(output)