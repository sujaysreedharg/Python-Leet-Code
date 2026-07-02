class Solution:
    def __init__(self):
        self.ans = []
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for i in range(n)] for _ in range(n)]
        self.backtrack(board,0)
        return self.ans
    
    def backtrack(self,board, row):
        if len(board) == row:
            
            layout = ["".join(board[i]) for i in range(len(board))]
            self.ans.append(layout)
            return 
        for col in range(len(board)):
            if not self.isvalidpos(board,row,col):
                continue
            board[row][col]="Q"
            self.backtrack(board,row+1)
            board[row][col]="."
            
    def isvalidpos(self,board,row,col):
        for r in range(len(board)):
            if board[r][col]=="Q":
                return False
        i=row-1
        j=col-1
        
        while i >=0 and j>=0:
            if board[i][j] == "Q":
                return False
            i-=1
            j-=1
        i=row-1
        j=col+1
        
        while i>=0 and j<len(board):
            if board[i][j] == "Q":
                return False
            i-=1
            j+=1
        return True
