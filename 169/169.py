class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        majority=None
        for n in nums:
            if count==0:
                majority=n
                count=1
            elif count>0:
                count=count+1 if majority == n else count-1

        return majority