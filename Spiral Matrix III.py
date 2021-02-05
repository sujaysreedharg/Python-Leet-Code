class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        row=r0
        col=c0
        direction=0
        maxlength=1
        length=maxlength
        output=[]
        move = [[0,1],[1,0],[0,-1],[-1,0]]
        while len(output)< R*C:
            while length:
                if 0<=row<R and 0<=col<C:
                    output.append([row,col])
                    print(length,direction)
                row+= move[direction][0]
                col+=move[direction][1]
                length-=1
            if direction== 1 or direction==3:
                maxlength+=1
            length=maxlength
            direction=(direction+1)%4
        return output
