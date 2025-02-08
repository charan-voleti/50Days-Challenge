class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        #sliding window technique
        l=r=0
        Sum=0
        n=len(nums)
        ans=0
        nums.sort()
        while r<n:
            Sum+=nums[r]
            while nums[r]*(r-l+1)>Sum+k:  #nums[r] * (r - l + 1) represents the total cost to    make all elements in [l, r] equal to nums[r].  
                                          #Sum + k represents the actual resources available to modify numbers in the range.
                Sum-=nums[l]
                l+=1
            ans=max(ans,r-l+1)
            r+=1
        return ans