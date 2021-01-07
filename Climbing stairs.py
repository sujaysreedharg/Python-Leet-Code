class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return n
        dp = [None]*(n+2)
        print(dp)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+2):
            dp[i]=dp[i-1]+dp[i-2]
            print(dp)
        return dp[-1]
        
   Time -> O(n)
   Space -> O(n)
   
