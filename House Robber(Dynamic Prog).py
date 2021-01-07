class Solution:
    def rob(self, nums):
        #Bottomup approach
        memo= [None]*(len(nums)+1)
        print(memo)
        memo[0]=0
        memo[1]=nums[0]
        for i in range(1,len(nums)):
            memo[i+1]=max((memo[i],memo[i-1]+nums[i]))
            print(memo)
        #memo=[0,1,2,4,,4]
        # nums =[1,2,3,1]
        return memo[-1]

Sol= Solution()
print(Sol.rob([1,2,3,1]))



Time -> O(n)
Space -> O(n)


