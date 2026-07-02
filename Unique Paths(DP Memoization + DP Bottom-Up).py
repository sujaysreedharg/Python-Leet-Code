# Recursion DFS without memoization | TME 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dparray = [[None for i in range(n)] for j in range(m)]
        return self.dfs(0,0,m,n)
    
    def dfs(self,r,c,m,n):
        if r>m-1 or c>n-1:
            return 0
        elif r==m-1 or c==n-1:
            return 1
        else:
            right= self.dfs(r,c+1,m,n)
            down=self.dfs(r+1,c,m,n)
            sum=right+down
            return sum
        
       
# DFS DP Memoization Top Down Approach 
# O(2^(m+n)) Time | O(mn) Space

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dparray = [[None for i in range(n)] for j in range(m)]
        return self.dfs(0,0,m,n,dparray)
    
    def dfs(self,r,c,m,n,dparray):
        if r>m-1 or c>n-1:
            return 0
        elif r==m-1 or c==n-1:
            return 1
        elif dparray[r][c] is not None:
            return dparray[r][c]
        else:    
            right= self.dfs(r,c+1,m,n,dparray)
            down=self.dfs(r+1,c,m,n,dparray)
            sum=right+down
            dparray[r][c]=sum
            return dparray[r][c]
          
          
# Bottom-Up Approach
# O(mn) Time | O(mn) Space  

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dparray = [[0 for i in range(n)] for j in range(m)]
        for r in range(m-1,-1,-1):
            for c in range(n-1,-1,-1):
                if c==n-1 or r==m-1:
                    dparray[r][c]=1
                else:
                    dparray[r][c]=dparray[r+1][c]+dparray[r][c+1]
        print(dparray)
        return dparray[0][0]
        
          
          
          
          
          
          
          
          
          
          
          
        
