class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev,r=0,0
        temp=x
        while(x>0):
            r=x%10
            rev=(rev*10)+r
            x//=10
        if temp==rev:
            return True
        else:
            return False
        