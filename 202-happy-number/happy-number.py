class Solution:
    def isHappy(self, n: int) -> bool:
        # helper function to calculate sum of squares of digits
        def get_next(num):
            total = 0
            while num > 0:
                r = num % 10
                total += r * r
                num //= 10
            return total

        slow = n
        fast = get_next(n)

        # loop until fast reaches 1 (happy number) OR fast meets slow (cycle)
        while fast != 1 and slow != fast:
            slow = get_next(slow)           # move 1 step
            fast = get_next(get_next(fast)) # move 2 steps

        return fast == 1
