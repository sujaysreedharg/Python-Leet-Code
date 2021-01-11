class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return
        rowlen=len(grid)
        collen=len(grid[0])
        for row in range(1,rowlen):
            grid[row][0]+=grid[row-1][0]
        for col in range(1,collen):
            grid[0][col]+=grid[0][col-1]
        for row in range(1,rowlen):
            for col in range(1,collen):
                grid[row][col]+=min(grid[row-1][col],grid[row][col-1])
        return grid[-1][-1]
