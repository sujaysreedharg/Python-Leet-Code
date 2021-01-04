class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = {i:set() for i in range(9)}
        col_dict = {j:set() for j in range(9)}
        grid_dict = {k:set() for k in range(9)}
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in row_dict[i]:
                        return False
                    row_dict[i].update(board[i][j])
                    if board[i][j] in col_dict[j]:
                        return False
                    col_dict[j].update(board[i][j])
                    currentgrid = i//3 * 3 + j//3
                    if board[i][j] in grid_dict[currentgrid]:
                        return False
                    grid_dict[currentgrid].update(board[i][j])
        return True
        
        
 Time complexity : O(1) since all we do here is just one iteration over the board with 81 cells.
Space complexity : (1).
