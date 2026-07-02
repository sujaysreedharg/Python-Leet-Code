class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[ 0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        k=s[::-1]
        
        for row in range(1,len(s)+1):
            for col in range(1,len(s)+1):
                if s[row-1] == k[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col],dp[row][col-1])
        lps=dp[-1][-1]
        return len(s) - lps
