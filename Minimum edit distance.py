class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        
        
        for r in range(len(word1)+1):
            for c in range(len(word2)+1):
                if r==0:
                    dp[r][c] = c
                elif c==0:
                    dp[r][c] = r
                elif word1[r-1]!=word2[c-1]:
                    dp[r][c] = min(dp[r-1][c-1]+1,dp[r][c-1]+1,dp[r-1][c]+1)
                else:
                    dp[r][c] = dp[r-1][c-1]
        return dp[-1][-1]
                
        
