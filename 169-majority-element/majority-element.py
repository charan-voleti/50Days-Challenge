class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        a=Counter(nums)
        for k,v in a.items():
            if v>(n/2):
                return k
        