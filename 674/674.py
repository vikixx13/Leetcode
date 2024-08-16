class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l=1
        mx=1
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                l+=1
                mx=max(mx,l)
            if (nums[i-1] == nums[i]) or (nums[i-1] > nums[i]):
                l=1
                mx=max(mx,l)
        return mx
