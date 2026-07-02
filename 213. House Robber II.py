class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        dp1=[-1 for _ in range(len(nums)-1)]
        dp2=[-1 for _ in range(len(nums)-1)]
        arr1=nums[1:]
        arr2=nums[:-1]
        def dfs(arr,i,dp):
            if dp[i]!=-1:
                return dp[i]
            if i==0:
                return arr[i]
            elif i<0:
                return 0
            pick=arr[i] + dfs(arr,i-2,dp)
            notpick=dfs(arr,i-1,dp)
            dp[i]=max(pick,notpick)
            return max(dp)

        return max(dfs(arr1,len(arr1)-1,dp1),dfs(arr2,len(arr2)-1,dp2))
                   
