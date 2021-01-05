class Solution:
    def uniquePaths(self, row_len: int, col_len: int) -> int:
        obstacleGrid=[[None for i in range(col_len)] for j in range(row_len)]
        obstacleGrid[0][0]=1
        

        for row in range(1,row_len):
            obstacleGrid[row][0]= 1
        for col in range(1,col_len):
            obstacleGrid[0][col]= 1 
        for row in range(1,row_len):
            for col in range(1,col_len):
                obstacleGrid[row][col]= obstacleGrid[row-1][col]+ obstacleGrid[row][col-1]

        return obstacleGrid[row_len-1][col_len-1]
        
        
        
        
        
        
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
        
        
        
        
