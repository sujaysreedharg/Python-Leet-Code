class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        print(dp)
        largest =0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]=="1":
                    dp[row][col] =  1 + min(dp[row-1][col],dp[row-1][col-1],dp[row][col-1])
                    if dp[row][col] > largest:
                        largest = dp[row][col]
        return largest*largest
