class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return(k)
        if k > numOnes and k <= numOnes+numZeros:
            return(numOnes)
        if k > numOnes+numZeros:
            min=k-numOnes-numZeros
            return(numOnes-min)