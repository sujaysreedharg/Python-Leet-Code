class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s= str1
        r=str2
        dp = [[[] for i in range(len(s)+1)] for j in range(len(r)+1)]
        for i in range(1,len(r)+1):
            for j in range(1,len(s)+1):
                if r[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + [r[i-1]]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1],key=len)
        lcs = dp[-1][-1]
        ans=''
        p1=0
        p2=0
        for ch in lcs:
            while str1[p1]!=ch:
                ans+= str1[p1]
                p1+=1
            while str2[p2]!=ch:
                ans+= str2[p2]
                p2+=1
            ans+=ch
            p1+=1
            p2+=1
        result = ans + str1[p1:] + str2[p2:]
        return result
