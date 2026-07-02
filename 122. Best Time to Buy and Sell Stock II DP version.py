class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        
        def rec(ind,buy,dp):
            if ind==len(prices):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]

            
            if buy:
                dp[ind][buy] = max(-prices[ind]+ rec(ind+1,0,dp), 0 + rec(ind+1,1,dp))
                
            else:
                dp[ind][buy] =  max(prices[ind]+ rec(ind+1,1,dp), 0 + rec(ind+1,0,dp))
                
            return dp[ind][buy]
        return rec(0,1,dp)
                
