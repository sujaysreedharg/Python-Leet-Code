class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums)%2)!=0:
            return False
        sumofarray=int(sum(nums)/2)
        print(sumofarray)
        dp=[[False for i in range(sumofarray+1)] for j in range(len(nums))]
        for row in range(len(nums)):
            dp[row][0]=True
        for col in range(1,sumofarray+1):
            dp[0][col]=nums[0]==col
        for row in range(1,len(nums)):
            for col in range(1,sumofarray+1):
                if dp[row-1][col]==True:
                    dp[row][col]=dp[row-1][col]
                elif nums[row]<=col:
                    dp[row][col]=dp[row-1][col-nums[row]]
        # print(dp)
        return dp[-1][-1]
        
