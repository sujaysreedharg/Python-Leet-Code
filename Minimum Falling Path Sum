Bottom-up:

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(0,len(matrix)):
            dp[0][i] = matrix[0][i]
        for i in range(1,len(matrix)):
            for j in range(0,len(matrix[0])):
                if j==0:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j],dp[i-1][j+1])
                elif 0<j<len(matrix[0])-1:
                    dp[i][j] = matrix[i][j]+ min(dp[i-1][j],dp[i-1][j+1],dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        ans= float("inf")
        for lastcol in range(0,len(matrix)):
            ans = min(ans,dp[len(matrix)-1][lastcol])
        return ans
        
        
        
Top-down Memoization:


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[float("inf") for i in range(len(matrix[0]))] for j in range(len(matrix))]
        ans = float("inf")

        def dfsrec(matrix,row,col):
            if row<0 or col <0 or row >= len(matrix) or col >= len(matrix[0]):
                return float("inf")
            if dp[row][col]!= float("inf"):
                return dp[row][col]
            if row+1 == len(matrix):
                dp[row][col]= matrix[row][col]
                return matrix[row][col]
            dp[row][col] = matrix[row][col] + min(dfsrec(matrix,row+1,col),dfsrec(matrix,row+1,col-1),dfsrec(matrix,row+1,col+1))
            return dp[row][col]
        for col in range(len(matrix[0])):
            ans = min(ans, dfsrec(matrix,0,col))
        return ans
