class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        boughtOn = prices[0]

        for day in prices[1:]:
            if day < boughtOn:
                boughtOn = day
                continue
            
            if day - boughtOn > maxProfit: maxProfit = day - boughtOn

        return maxProfit