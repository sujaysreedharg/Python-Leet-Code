class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rowlen = len(board)
        collen = len(board[0])
        def dfs(row,col):
            if 0<=row<=rowlen-1 and 0<=col<=collen-1 and board[row][col]=="O":
                board[row][col]="."
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col-1)
                dfs(row,col+1)
        
        for row in range(rowlen):
            if board[row][0]=="O":
                dfs(row,0)
            if board[row][collen-1]=="O":
                dfs(row,collen-1)
        
        for col in range(collen):
            if board[0][col]=="O":
                dfs(0,col)
            if board[rowlen-1][col]=="O":
                dfs(rowlen-1,col)
                
        for row in range(rowlen):
            for col in range(collen):
                if board[row][col]=="O":
                    board[row][col]="X"
                if board[row][col]==".":
                    board[row][col]="O"
