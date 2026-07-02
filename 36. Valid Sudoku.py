class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        grids=collections.defaultdict(set)
        #we can use a list instead of set but a set provides constant lookup time like hashmap unlike list which has to iterate over all values to find if an element is present. sets are not accessible like array[0] because they are unordered. However, if we iterate over a set and a list separately, a list is faster because it is ordered in memory.
        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    continue
                if (board[row][col] in rows[row] or 
                    board[row][col] in cols[col] or 
                    board[row][col] in grids[(row//3,col//3)]):
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                grids[(row//3,col//3)].add(board[row][col])
        
        return True
                
