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

    
    
    Dijkstra Solution:
    
    class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        visited=[[False for j in range(len(grid[0]))] for i in range(len(grid))]
        pq = [(grid[0][0],0,0)]
        rowlen= len(grid)
        collen = len(grid[0])
        ans = grid[0][0]
        while pq:
            dis,row,col = heapq.heappop(pq)

            ans = max(ans,dis)
            if row == rowlen-1 and col == collen-1:
                break
            for friends in [(0,-1),(-1,0),(0,1),(1,0)]:
                r = row + friends[0]
                c = col + friends[1]
                if  not (r<0 or c<0 or r>rowlen-1 or c>collen-1) and visited[r][c]==False:
                    visited[r][c]=True
                    heapq.heappush(pq,(grid[r][c],r,c))
        return ans
                        
