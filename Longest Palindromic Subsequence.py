class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        def lcs(s,r):
            dp=[[0 for i in range(len(s)+1)] for j in range(len(r)+1)]
            for i in range(1,len(r)+1):
                for j in range(1,len(s)+1):
                    if r[i-1]==s[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            return dp[-1][-1]
        return lcs(s,s[::-1])
        
        
        
        
        Time -> O(nm*min(n,m))
        Space -> O(nm*min(n,m))
