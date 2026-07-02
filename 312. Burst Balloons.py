class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #k is the last element that we pop.
        dp=[[-1 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
        nums=[1] + nums +[1]
        def dfs(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if i-1 <0:
                left=1
            else:
                left=nums[i-1]
            if j+1>=len(nums):
                right=1
            else:
                right=nums[j+1]
            result=0
            for k in range(i,j+1):
                
                result = max(result, left*nums[k]*right + dfs(i,k-1)+dfs(k+1,j))
            dp[i][j] = result
            return dp[i][j]
        return dfs(1,len(nums)-2)
