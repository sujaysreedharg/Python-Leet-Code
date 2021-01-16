class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for indrow in range(numRows):
            row = [None  for  _ in range(indrow+1)]
            row[0],row[-1]=1,1
            for j in range(1,indrow):
                           
                row[j]=triangle[indrow-1][j-1]+triangle[indrow-1][j]
            triangle.append(row)
        return triangle
