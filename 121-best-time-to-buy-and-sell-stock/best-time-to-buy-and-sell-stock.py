class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_stock=prices[0]
        for i in range(1,len(prices)):
            val=prices[i]-min_stock
            if val>profit:
                profit=val
            min_stock=min(min_stock,prices[i])
        return profit

        