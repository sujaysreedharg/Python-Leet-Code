class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1 for _ in range(2)] for _ in range(len(prices)+1)]
        profit=0
        def dfs(idx,buy):
            if idx>=len(prices):
                return 0
            if dp[idx][buy]!=-1:
                return dp[idx][buy]
            if buy:
                dp[idx][buy]= max(-prices[idx] + dfs(idx+1,0), dfs(idx+1,1))
            else:
                dp[idx][buy]= max(prices[idx]+ dfs(idx+2,1), dfs(idx+1,0))
            return dp[idx][buy]
        return dfs(0,1)
    
