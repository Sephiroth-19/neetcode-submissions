class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(1 , len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            else:
                a = prices[i] - min_price
                if a > max_profit:
                    max_profit = a
                else:
                    continue
        if max_profit > 0:
            return max_profit
        else:
            return 0
            
