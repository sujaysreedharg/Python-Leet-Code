class Solution:
    def __init__(self, row_len = 0, col_len = 0):
        #total rows and cols and init board holds values at a clean state before iterations state
        self.row_len = row_len
        self.col_len = col_len 
        self.originalarray = [[]]
        
        #immutable const
        self.neighbours  = [[1,0],[0,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        #magic numbers
        self.alive = 1
        self.dead = 0
    def gameOfLife(self, board: List[List[int]]) -> None:
        self.row_len = len(board)
        self.col_len = len(board[0])
        self.originalarray = [[board[j][i] for i in range(self.col_len)] for j in range(self.row_len)]
        for i in range(self.row_len):
            for j in range(self.col_len):
                countliveneighbours = self.neighcounter(i,j)
                if countliveneighbours > 3 or countliveneighbours < 2:
                    board[i][j] = self.dead

                else:
                    if board[i][j]==self.dead:
                        if countliveneighbours==3:
                            board[i][j]= self.alive
                
                
    def neighcounter(self,row,col):
        counter=0
        for n in self.neighbours:
            r = row + n[0]
            c = col + n[1]
            if r < self.row_len and r >=0 and c < self.col_len and c >=0:
                if self.originalarray[r][c] == self.alive:
                    counter+=1
        return counter
