class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1 for _ in range(len(nums))]
        def dfs(i):
            if dp[i]!=-1:
                return dp[i]
            if i==0:
                return nums[i]
            elif i<0:
                return 0
            pick=nums[i] + dfs(i-2)
            notpick=dfs(i-1)
            dp[i]=max(pick,notpick)
            return max(dp)
        
        return dfs(len(nums)-1)
            
        
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1 for _ in range(len(nums))]
        dp[0]=nums[0]
        # dp=[1,2,4,4]
        for i in range(1,len(nums)):
            if i>1:
                nextval=dp[i-2]
            else:
                nextval=0
            take = nums[i] + nextval
            nottake = dp[i-1]
            dp[i] = max(take,nottake)
            
        # print(dp)
        return max(dp)
            
