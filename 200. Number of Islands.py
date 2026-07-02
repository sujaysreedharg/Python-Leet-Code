class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row,col):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]):
                return 
            elif grid[row][col]=="0":
                return
            elif grid[row][col]=="1":
                grid[row][col]="0"
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row,col-1)
            dfs(row-1,col)
        
        result=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=="1":
                    result+=1
                    dfs(row,col)
        return result
