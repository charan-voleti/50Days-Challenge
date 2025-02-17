class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not  strs:
            return ""
        pre=strs[0]
        pl=len(pre)
        for i in strs[1:]:
            while pre[:pl]!=i[:pl]:
                pl-=1
                if pl==0:
                    return ""
                pre=pre[:pl]
        return pre[:pl]
        