class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if  matrix[row][col]==0:
                    for i in range(len(matrix[0])):
                        if i!=col and matrix[row][i]==0:
                            matrix[row][i]=2**32
                        else:
                            matrix[row][i]=2**31
                    for j in range(len(matrix)):
                        if j!=row and matrix[j][col]==0:
                            matrix[j][col]=2**32
                        else:
                            matrix[j][col]=2**31
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if  matrix[row][col]==2**32:
                    matrix[row][col]=2**31
                    for i in range(len(matrix[0])):
                        if matrix[row][i]!=2**32:
                            matrix[row][i]=2**31
                    for j in range(len(matrix)):
                        if matrix[j][col]!=2**32:
                            matrix[j][col]=2**31
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==2**31:
                    matrix[row][col]=0
                            
        return matrix
    
    
                        
        
