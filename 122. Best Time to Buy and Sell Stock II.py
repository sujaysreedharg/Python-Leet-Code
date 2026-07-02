class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        length = len(prices)-1
        profit=0
        buy=0
        sell=0
        while i<length:
            while(i<length and  prices[i]>=prices[i+1]):
                i+=1
            buy = prices[i]
            while(i< length and prices[i] <=prices[i+1]):
                i+=1
            sell = prices[i]
            profit+=sell-buy
        return  profit
        
