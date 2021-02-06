class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_len =len(matrix)
        col_len = len(matrix[0])
        resultpath=[]
        dp = [[-1 for i in range(col_len)] for j in range(row_len)]
        for i in range(0,row_len):
            for j in range(0,col_len):
                print(i,j)
                resultpath.append(self.dfs(matrix,i,j,1,dp))
        print(resultpath)
        return max(resultpath)
        
    def dfs(self,matrix,i,j,currmax,dp):

        if dp[i][j]!=-1: 
            return dp[i][j]
        else:
            

            if j and matrix[i][j]>matrix[i][j-1]:
                left =self.dfs(matrix,i,j-1,currmax,dp)

            else: 
                left= 0

            if i and  matrix[i][j]>matrix[i-1][j]:
                up=self.dfs(matrix,i-1,j,currmax,dp)
            else: 
                up= 0

            if i<len(matrix)-1 and matrix[i][j]>matrix[i+1][j]:
                down =self.dfs(matrix,i+1,j,currmax,dp)
            else: 
                down= 0

            if j <len(matrix[0])-1 and matrix[i][j]>matrix[i][j+1]:

                right=self.dfs(matrix,i,j+1,currmax,dp)
            else:
                right= 0
            dp[i][j]= 1 + max(up,down,left,right)
        return dp[i][j]
