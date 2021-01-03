class Solution:
    def solution(self,board,row,col,value):
        for i in range(9):
            if board[row][i]==str(value):
                return False
        for j in range(9):
            if board[j][col]==str(value):
                return False
        gridrow= row//3
        gridcol=col//3
        for i in range(3):
            for j in range(3):
                if board[3*gridrow+i][3*gridcol+j]==str(value):
                    return False
        return True
    
    def backtrack(self,board):
        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    for value in range(9):
                        if self.solution(board,row,col,value+1):
                            board[row][col]= str(value+1)
                            if self.backtrack(board):
                                return True
                            else:
                                board[row][col]="."
                    else:
                        return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
