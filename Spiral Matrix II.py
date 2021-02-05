class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top=0
        down= n-1
        left=0
        right=n-1
        count=1
        ans=[[0 for i in range(n)] for j in range(n)]
        while top<=down and left<=right:
            for i in range(left,right+1):
                ans[top][i]=count
                count+=1
            top+=1
            for i in range(top,down+1):
                ans[i][right]=count
                count+=1
            right-=1
            for i in range(right,left-1,-1):
                ans[down][i]=count
                count+=1
            down-=1
            for i in range(down,top-1,-1):
                ans[i][left]=count
                count+=1
            left+=1
        return ans
