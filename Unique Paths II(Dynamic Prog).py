class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0]=1
        
        row_len = len(obstacleGrid)
        col_len = len(obstacleGrid[0])
        for row in range(1,row_len):
            obstacleGrid[row][0]= 1 if (obstacleGrid[row][0]== 0 and obstacleGrid[row-1][0]==1) else 0
        for col in range(1,col_len):
            obstacleGrid[0][col]= 1 if (obstacleGrid[0][col]==0 and obstacleGrid[0][col-1]==1) else 0
        for row in range(1,row_len):
            for col in range(1,col_len):
                if obstacleGrid[row][col]==0:
                    obstacleGrid[row][col]= obstacleGrid[row-1][col]+ obstacleGrid[row][col-1]
                else:
                    obstacleGrid[row][col]=0
        return obstacleGrid[row_len-1][col_len-1]
        
        
Time -> O(m*n)
Space -> O(1)
        
      A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
