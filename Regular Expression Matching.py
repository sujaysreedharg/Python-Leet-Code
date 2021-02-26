class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        if not s and not p:
            return True
        for row in range(1,len(dp)):
            dp[row][0] = False
        for col in range(1,len(dp[0])):
            if p[col-1]=="*" and col>1:
                dp[0][col] = dp[0][col-2]
            else:
                dp[0][col]=False
        
        for row in range(1,len(dp)):
            for col in range(1,len(dp[0])):
                if s[row-1] == p[col-1] or p[col-1]==".":
                    dp[row][col]=dp[row-1][col-1]
                elif col>1 and p[col-1]=="*":
                    if dp[row][col-2]==True:
                        dp[row][col]= True
                    elif s[row-1]==p[col-2] or p[col-2]==".":
                        dp[row][col]= dp[row-1][col]
                    else:
                        dp[row][col]=False
                else:
                    dp[row][col]= False
        return dp[-1][-1]
                    
