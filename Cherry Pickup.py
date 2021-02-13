class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        result = self.dfsrec(0,0,0,0,len(grid),grid,{})
        return result if result!=float("-inf") else 0
    def dfsrec(self,x1,y1,x2,y2,n,grid,memset):
        cherries=0
        if x1==n or x2==n or y1 ==n or y2==n or grid[x1][y1]==-1 or grid[x2][y2]==-1:
            return float("-inf")
        if (x1,y1,x2,y2) in memset:
            return memset[(x1,y1,x2,y2)]
        elif x1==x2==y1==y2==n-1:
            return grid[x1][y1]
        else:
            if x1==x2 and y1==y2:
                cherries = grid[x1][y1]
            else:
                cherries = grid[x1][y1]+grid[x2][y2]
            memset[(x1,y1,x2,y2)] = cherries + max(self.dfsrec(x1+1,y1,x2+1,y2,n,grid,memset),
                                               self.dfsrec(x1,y1+1,x2,y2+1,n,grid,memset),
                                               self.dfsrec(x1+1,y1,x2,y2+1,n,grid,memset),
                                               self.dfsrec(x1,y1+1,x2+1,y2,n,grid,memset))
            return memset[(x1,y1,x2,y2)]
            
