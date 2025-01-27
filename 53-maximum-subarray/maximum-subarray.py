class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c,m=nums[0],nums[0]
        for i in nums[1:]:
            c=max(i,c+i)
            m=max(c,m)
        return m


        