class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=set()
        i=0
        while i<len(nums):
            if nums[i] in num:
                nums.pop(i)
            else:
                num.add(nums[i])
                i+=1
        return len(nums)
        