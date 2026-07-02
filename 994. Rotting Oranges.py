class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        r = len(grid)
        c= len(grid[0])
        fresh =0
        levels =0
        dq= collections.deque()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        
        for row in range(r):
            for col in range(c):
                if grid[row][col]==1:
                    fresh+=1
                elif grid[row][col]==2:
                    dq.append((row,col))
        
        while dq:
            levels+=1
            for _ in range(len(dq)):
                x,y = dq.popleft()
                
                for dx,dy in dirs:
                    if 0<=x+dx<r and 0<= y+dy<c and grid[x+dx][y+dy]==1:
                        fresh-=1
                        grid[x+dx][y+dy]=2
                        dq.append((x+dx,y+dy))
        return -1 if fresh!=0 else max(levels-1,0)
