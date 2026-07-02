class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        def backtrack(zeros,r,c):
            if r<0 or c<0 or r==len(grid) or c==len(grid[0]) or grid[r][c]==-1:
                return 0
            if grid[r][c]==2:
                if zeros==-1:
                    return 1
                else:
                    return 0
            grid[r][c]=-1
            zeros-=1
            total = backtrack(zeros,r+1,c) + backtrack(zeros,r-1,c) + backtrack(zeros,r,c+1) + backtrack(zeros,r,c-1)
            grid[r][c]=0
            zeros+=1
            
            return total
        
        
        
        zeros,sx,sy= 0,0,0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    zeros+=1
                if grid[r][c]==1:
                    sx=r
                    sy=c
        return backtrack(zeros,sx,sy)
        
                           

        
