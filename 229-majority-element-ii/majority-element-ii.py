class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=Counter(nums)
        r=[]
        for k,v in a.items():
            if v>(n/3):
                r.append(k)
        return r
                
            

        