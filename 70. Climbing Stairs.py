class Solution:
    def climbStairs(self, n: int) -> int:
        res=0
        memset={}
        def dfs(amount):
            if amount==0:
                return 1
            if amount < 0:
                return 0
            if amount in memset:
                return memset[amount]
            memset[amount]= dfs(amount-1) + dfs(amount-2)
            return memset[amount]
        return dfs(n)
