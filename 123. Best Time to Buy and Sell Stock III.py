class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[[0 for i in range(3)]for j in range(2)]for k in range(len(prices)+1)]
        for idx in range(len(prices)-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy:
                        dp[idx][buy][cap]=max(-prices[idx]+ dp[idx+1][0][cap],dp[idx+1][1][cap])
                    else:
                        dp[idx][buy][cap]=max(prices[idx] +dp[idx+1][1][cap-1],dp[idx+1][0][cap])
        return dp[0][1][2]              
                
          
          
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[[-1 for i in range(3)]for j in range(2)]for k in range(len(prices)+1)]

        def dfs(idx,buy,cap,dp):
            if idx==len(prices):
                return 0
            if cap==0:
                return 0
            if dp[idx][buy][cap]!=-1:
                return dp[idx][buy][cap]
            if buy:
                dp[idx][buy][cap]=max(-prices[idx]+ dfs(idx+1,0,cap,dp),dfs(idx+1,1,cap,dp))
                return dp[idx][buy][cap]
            else:
                dp[idx][buy][cap]=max(prices[idx] + dfs(idx+1,1,cap-1,dp),dfs(idx+1,0,cap,dp))
                return dp[idx][buy][cap]
            
        return dfs(0,1,2,dp)        
          
          
