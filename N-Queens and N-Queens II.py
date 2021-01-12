class Solution:
    def __init__(self):
        self.ans=[]
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        self.dfsbacktrack(board,0)
        return self.ans
    def dfsbacktrack(self,board,row):
        if len(board)==row:
            layout = ["".join(board[i]) for i in range(len(board))]
            self.ans.append(layout)
            return
        for col in range(len(board)):
            if not self.is_valid_position(board,row,col):
                continue
            board[row][col]="Q"
            self.dfsbacktrack(board,row+1)
            board[row][col]="."
    def is_valid_position(self,board,row,col):
        #top to down
        for r in range(len(board)):
            if board[r][col]=="Q":
                return False
        #upper left
        i=row-1
        j=col-1
        while i>=0 and j>=0:
            if board[i][j]=="Q":
                return False
            i-=1
            j-=1
        #upper right
        i=row-1
        j=col+1
        while i>=0 and j<len(board):
            if board[i][j]=="Q":
                return False
            i-=1
            j+=1
        return True
    
    
 For N-Queens II : Just initialize self.ans=0 and change the base case to  self.ans+=1
