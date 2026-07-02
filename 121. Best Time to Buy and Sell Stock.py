class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxprofit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit= prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
            else:
                while prices[l]>prices[r]:
                    l+=1
            r+=1
        return maxprofit

    
    #DP Kadane
    
    
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxsofar=0
        maxendinghere=0
        for i in range(1,len(prices)):
            maxendinghere=max(0,maxendinghere+prices[i]-prices[i-1])
            maxsofar=max(maxendinghere,maxsofar)
            
        return maxsofar
            
