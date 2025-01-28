class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=0
        set_1=set(nums)
        for i in set_1:
            if (i-1) not in set_1:
                l=1
                while(i+l in set_1):
                    l+=1
                m=max(m,l)
        return m
        