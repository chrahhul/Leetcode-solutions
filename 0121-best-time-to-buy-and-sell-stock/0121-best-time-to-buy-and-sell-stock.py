class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxp=0
        for price in prices:
            minp=min(minp,price)
            maxp=max(maxp,price-minp)
        return maxp
    
    
    
        