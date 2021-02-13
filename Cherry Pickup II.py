class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])
        
        
        def dfs(row,col1,col2,cache):
            if (row,col1,col2) in cache:
                return cache[(row,col1,col2)]
            elif col1<0 or col1>col-1 or col2<0 or col2 > col-1:
                return float("-inf")
            cherries =0
            cherries+= grid[row][col1]
            if col1!=col2:
                cherries+=grid[row][col2]
            temp=0
            if row!=rows-1:
                for m1 in (col1,col1-1,col1+1):
                    for m2 in (col2,col2-1,col2+1):
                        temp = max(temp,dfs(row+1,m1,m2,cache))
            result = cherries+ temp
            cache[(row,col1,col2)] = result
            return cache[(row,col1,col2)]
              
        result= dfs(0,0,col-1,{})
        return result
                           
