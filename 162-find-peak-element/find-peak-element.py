class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        a=max(nums)
        b=nums.index(a)
        return b
