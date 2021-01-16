class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp=[0 for i in range(len(s))]
        maxans=0
        for i in range(1,len(s)):
            if s[i]==")":
                if i >=2 and s[i-1]=="(":
                    dp[i]= dp[i-2]+2
                elif i<2 and s[i-1]=="(":
                    dp[i]+=2
                elif (i-dp[i-1])> 0 and  s[i-dp[i-1]-1]=="(":
                    
                    dp[i]=  dp[i-1]+2 + dp[i-dp[i-1]-2]

            maxans = max(maxans,dp[i])
        return maxans
        
        
        O(n) -> Time
        O(n) -> Space
