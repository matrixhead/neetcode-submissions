class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l = 0
        for r in range(1,len(prices)):
            np = prices[r]-prices[l]
            profit = np if np > profit else profit
            l = r if prices[r] < prices[l] else l
            
        return profit