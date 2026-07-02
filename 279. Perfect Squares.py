class Solution:
    def numSquares(self, n: int) -> int:
        if n<=3:
            return n
        dp=[i for i in range(n+1)]
        
        for i in range(len(dp)):
            for j in range(1,i):
                if j*j>i:
                    break
                dp[i]=min(dp[i],1+dp[i-j*j])
                
        return dp[-1]
        
        
