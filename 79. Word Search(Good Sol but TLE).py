class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def backtrack(row,col,idx):
            if idx==len(word):
                return True
            elif row<0 or row>=len(board) or col<0  or col>=len(board[0]) or visited[row][col] or board[row][col]!=word[idx] :
                return False
            visited[row][col]=True
            if ( backtrack(row+1,col,idx+1) or backtrack(row,col+1,idx+1) or backtrack(row-1,col,idx+1) or backtrack(row,col-1,idx+1)):
                return True
            visited[row][col]=False
            return False
            
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]==word[0] and backtrack(row,col,0,):
                    return True
        return False
        
