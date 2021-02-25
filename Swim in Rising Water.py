class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        def dfs(i,j,mid,visited):
            visited[i][j] = True
            for dir in [(0,-1),(-1,0),(0,1),(1,0)]:
                row = i+dir[0] 
                col= j+dir[1]
                if  not (row<0 or col< 0 or row>len(grid)-1 or col>len(grid[0])-1) and not visited[row][col] and grid[row][col]<=mid:
                    if row==len(grid)-1 and col==len(grid[0])-1:
                        return True
                    if dfs(row,col,mid,visited):
                        return True
            return False
        
                    
        low = grid[0][0]
        N= len(grid)
        high = N*N-1
        while low<high:
            mid = (low+high)//2
            visited=[[False for j in range(len(grid[0]))] for i in range(len(grid))]
            if dfs(0,0,mid,visited):
                high = mid
            else:
                low= mid+1
        return low
