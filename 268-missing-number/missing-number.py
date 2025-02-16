class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        osum=0
        asum=0
        n=len(nums)
        for i in range(1,n+1):
            osum+=i
        asum=sum(nums)
        return osum-asum      