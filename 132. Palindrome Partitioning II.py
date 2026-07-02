#TOP DOWN TLE
class Solution:
    def minCut(self, s: str) -> int:
        dp =[-1 for _ in range(len(s))]
        def ispalindrome(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def dfs(ind):
            # print(ind)
            if ind==len(s):
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            mincut = float("inf")
            for i in range(ind,len(s)):
                if ispalindrome(ind,i):
                    cuts = 1 + dfs(i+1)
                    mincut = min(cuts, mincut)
            dp[ind]=mincut
            return dp[ind]
        return dfs(0)-1
                   
        
class Solution:
    def minCut(self, s: str) -> int:
        dp =[0 for _ in range(len(s)+1)]
        def ispalindrome(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        for n in range(len(s)-1,-1,-1):
            mincut = float("inf")
            for i in range(n,len(s)):
                if ispalindrome(n,i):
                    cuts = 1 + dp[i+1]

                    mincut = min(cuts, mincut)
            dp[n]=mincut
        return dp[0]-1
