class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        s1=str1
        s2=str2
        
        dp=[[[] for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
        
        for i in range(1,len(s2)+1):
            for j in range(1,len(s1)+1):
                if s2[i-1]==s1[j-1]:
                    dp[i][j] = dp[i-1][j-1] + [s2[i-1]]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1],key=len)
        lcs=dp[-1][-1]
        p1,p2=0,0
        ans=""
        # print(lcs)
        for ch in lcs:
            while str1[p1]!= ch:
                ans+=str1[p1]
                p1+=1
            while str2[p2]!=ch:
                ans+=str2[p2]
                p2+=1
            ans+=ch
            p1+=1
            p2+=1
        ans+= s1[p1:] + s2[p2:]
        return ans
                
                
        
        
        
