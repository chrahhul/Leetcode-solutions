class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=float("inf")
        for price in prices:
            minp=min(price,minp)
            maxp=max(maxp,price-minp)
        return maxp
        