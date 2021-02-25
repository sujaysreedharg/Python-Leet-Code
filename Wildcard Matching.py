class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        if not s and not p:
            return True
        if len(p) - p.count('*') > len(s):
            return False
        for row in range(1,len(dp)):
            dp[row][0] = False
        for col in range(1,len(dp[0])):
            if p[col-1]=="*":
                dp[0][col] = dp[0][col-1]
        print(dp)
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                if s[row-1]==p[col-1] or p[col-1]=="?":
                    dp[row][col] = dp[row-1][col-1]
                elif p[col-1]=="*":
                        dp[row][col] = dp[row-1][col] or dp[row][col-1]
                else:
                    dp[row][col] = False
        return dp[-1][-1]
