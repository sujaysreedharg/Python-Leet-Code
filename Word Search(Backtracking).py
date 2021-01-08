class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        visited= [[False for i in range(col_len)] for j in range(row_len)]
        print(visited)
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col]== word[0] and self.dfsbacktracking(board,row,col,0,word,visited):
                    return True
        return False
    def dfsbacktracking(self,board,row,col,currentidxofword,word,visited):
        
        if currentidxofword==len(word):
            return True
        
        if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or visited[row][col] or board[row][col]!= word[currentidxofword]:
            return False
        
        visited[row][col]=True
        if ( self.dfsbacktracking(board,row+1,col,currentidxofword+1,word,visited) or
            self.dfsbacktracking(board,row-1,col,currentidxofword+1,word,visited) or
            self.dfsbacktracking(board,row,col+1,currentidxofword+1,word,visited) or
            self.dfsbacktracking(board,row,col-1,currentidxofword+1,word,visited)):
            return True
        visited[row][col]=False
        return False
