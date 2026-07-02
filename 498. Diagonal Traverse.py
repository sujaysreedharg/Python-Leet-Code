class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        up=True
        result=[]
        m=len(mat)
        n=len(mat[0])
        row=0
        col=0
        while row<m and col<n:
            if up:
                while row>0 and col<n-1:
                    result.append(mat[row][col])
                    row-=1
                    col+=1
                result.append(mat[row][col])
                if col==n-1:
                    row+=1
                else:
                    col+=1
            else:
                while row<m-1 and col>0:
                    result.append(mat[row][col])
                    row+=1
                    col-=1
                result.append(mat[row][col])

                if row==m-1:
                    col+=1
                else:
                    row+=1
            if up is False:
                up= True
            else:
                up=False
        return result
                
                
                
        
        
