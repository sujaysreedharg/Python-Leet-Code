Bottom-up:

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n= len(arr)
        m = len(arr[0])
        for i in range(1,n):        
            min1 = min(arr[i-1])
            min1idx = arr[i-1].index(min1)
            min2 = min(x for j,x in enumerate(arr[i-1]) if j!=min1idx)
            for j in range(m):
                if arr[i-1][j]==min1:
                    arr[i][j]+= min2
                else:
                    arr[i][j]+=min1
        return min(arr[-1])








Working Code(DFS Recursive Memo DP approach) : TLE if runtime is too strict or too many test cases

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        dp = [[-1 for i in range(len(arr[0]))] for j in range(len(arr))]
        def memo(arr,row,col):
            if row== len(arr):
                return 0
            if dp[row][col]!= -1:
                return dp[row][col]
            insideans = float("inf")
            for currcol in range(len(arr[0])):
                if currcol!= col:
                    insideans = min(insideans,memo(arr,row+1,currcol))
            dp[row][col] = arr[row][col]+ insideans
            return dp[row][col]
        ans = float("inf")
        for col in range(len(arr[0])):
            ans = min(ans,memo(arr,0,col))
        return ans
