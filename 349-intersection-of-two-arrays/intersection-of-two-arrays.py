class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen={}
        res=[]
        for num in nums1:
            if num not in seen:
                seen[num]=1
        for num in set(nums2):
            if num in seen:
                res.append(num)
        return res

        