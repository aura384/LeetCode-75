class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1 # left is buying, right is selling (two pointers)
        maximumProfit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maximumProfit = max(maximumProfit, profit)
            else:
                left = right # left needs to be the lowest possible value
            right += 1
        return maximumProfit
