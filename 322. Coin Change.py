class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf") for _ in range(amount+1)]
        dp[0]=0
        for eachcoin in coins:
            for eachamt in range(amount+1):
                if eachcoin <= eachamt:
                    dp[eachamt]=min(dp[eachamt],1+ dp[eachamt-eachcoin])
        return dp[-1] if dp[-1]!=float('inf') else -1
        
        
