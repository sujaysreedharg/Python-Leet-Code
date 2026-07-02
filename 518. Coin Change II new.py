class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp= [[0 for i in range(amount+1)] for _ in range(len(coins)+1)]
        for r in range(len(coins)+1):
            dp[r][0] = 1
        for r in range(1,len(coins)+1):
            for c in range(1,amount+1):
                if coins[r-1]<=c:
                    dp[r][c] = dp[r-1][c] + dp[r][c-coins[r-1]]
                else:
                    dp[r][c] = dp[r-1][c]
        return dp[-1][-1]
