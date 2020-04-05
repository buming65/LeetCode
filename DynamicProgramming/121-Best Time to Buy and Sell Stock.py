class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = 0
        for i in prices:
            if i < min_price:
                min_price = i
            elif i - min_price > max_price:
                max_price = i - min_price
        return max_price