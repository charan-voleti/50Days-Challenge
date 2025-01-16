class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=mc=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                mc=max(c,mc)
            else:
                c=0
        return mc


        