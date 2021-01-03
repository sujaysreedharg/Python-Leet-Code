class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh={}
        rotten={}
        move = [[1,0],[0,1],[-1,0],[0,-1]]
        minutes=0
        row = len(grid)
        col = len(grid[0])
        for i in range (row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh[i,j]=1
                elif grid[i][j]==2:
                    rotten[i,j]=1
        if not fresh:
            return 0
        while fresh:
            currot={}
            for coor in rotten:
                for m in move:
                    i= coor[0]+m[0]
                    j= coor[1]+m[1]
                    if (i,j) in fresh:
                        del fresh[i,j]
                        currot[i,j]=1
            if not currot:
                return -1
            rotten=currot
            minutes+=1
        return minutes
        
        
        https://leetcode.com/problems/rotting-oranges/
