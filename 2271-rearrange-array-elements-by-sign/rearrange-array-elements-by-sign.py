class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p=[]
        n=[]
        an=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        for i in range(len(p)):
            an.append(p[i])
            an.append(n[i])
        return an
        