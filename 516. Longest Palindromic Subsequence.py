class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        
        def lcs(s1,s2):
            for i in range(1,len(s1)+1):
                for k in range(1,len(s1)+1):
                    if s1[i-1] == s2[k-1]:
                        dp[i][k] = 1 + dp[i-1][k-1]
                    else:
                        dp[i][k] = max(dp[i-1][k],dp[i][k-1])
            return dp[-1][-1]
        
        return lcs(s, s[::-1])
