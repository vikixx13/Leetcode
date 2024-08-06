class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        if n % 2 == 1:
            return float(nums1[n//2])
        elif n % 2 == 0:
            x=int(n/2)
            y=int(n/2)-1
            sol = float(nums1[x] + nums1[y])/2
            return sol