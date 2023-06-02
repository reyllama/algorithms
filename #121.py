"""
2023.06.02
"""
"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 10**4
        res = 0
        for price in prices:
            if price < cur:
                cur = price
            elif price > cur:
                res = max(res, price-cur)
        return res

"""
Time > 82.79%, Memory > 39.65%
"""