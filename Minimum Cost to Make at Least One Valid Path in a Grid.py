class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rowlen = len(grid)
        collen = len(grid[0])
        pq = [(0,0,0)]
        seen =set()
        while pq:
            cost,row,col = heapq.heappop(pq)
            if (row,col) in seen: continue
            seen.add((row,col))
            if row == len(grid)-1 and col == len(grid[0])-1:
                return cost
            if col<collen-1:
                heapq.heappush(pq,(cost+(grid[row][col]!=1),row,col+1))
            if col>0:
                heapq.heappush(pq,(cost+(grid[row][col]!=2),row,col-1))
            if row<rowlen-1: 
                heapq.heappush(pq,(cost+(grid[row][col]!=3),row+1,col))
            if row>0:
                heapq.heappush(pq,(cost+(grid[row][col]!=4),row-1,col))
        return -1
        
