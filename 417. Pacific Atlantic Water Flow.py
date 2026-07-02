class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        res=[]
        pac,alt =set(),set()
        
        
        def dfs(r,c,prev,visit):
            if (r,c) in visit or r<0 or c<0 or r==ROWS or c == COLS or heights[r][c] < prev:
                return
            visit.add((r,c))
            dfs(r+1,c,heights[r][c],visit)
            dfs(r,c+1,heights[r][c],visit)
            dfs(r-1,c,heights[r][c],visit)
            dfs(r,c-1,heights[r][c],visit)

        
        for c in range(COLS):
            dfs(0,c,heights[0][c],pac)
            dfs(ROWS-1,c,heights[ROWS-1][c],alt)
        for r in range(ROWS):
            dfs(r,0,heights[r][0], pac)
            dfs(r,COLS-1, heights[r][COLS-1],alt)
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in alt:
                    res.append((r,c))
        return res
            
