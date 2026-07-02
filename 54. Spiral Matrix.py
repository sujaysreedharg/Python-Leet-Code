class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,top=0,0
        right,down=len(matrix[0])-1, len(matrix)-1
        result=[]
        dir=0
        while(top <= down) and (left<=right):
            
            if dir==0: 
                for i in range(left,right+1):
                    result.append(matrix[top][i])
                top+=1
            elif dir==1:
                for i in range(top,down+1):
                    result.append(matrix[i][right])  
                right-=1
            elif dir==2:
                for i in range(right,left-1,-1):
                    result.append(matrix[down][i])
                down-=1
            elif dir==3:
                for i in range(down,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
            dir=(dir+1)%4
        return result
                
