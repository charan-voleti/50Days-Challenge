class Solution:
    def reverse(self, x: int) -> int:
        temp=abs(x)
        rev=0
        while(temp>0):
            r=temp%10
            rev=(rev*10)+r
            temp//=10
        if -2**31<=rev<=(2**31)-1:
            if x<0:
                return -rev
            else:
                return rev
        else:
            return 0
        