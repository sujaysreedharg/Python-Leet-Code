class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums%2!=0:
            return False
        sumog = int(sums/2)
        n=len(nums)
        dp = [[False for i in range(sumog+1)] for j in range(n)]
        for row in range(n):
            dp[row][0]=True
        for col in range(1,sumog+1):
            dp[0][col]= nums[0]==col
        for row in range(1,len(nums)):
            for col in range(1,sumog+1):
                if dp[row-1][col]==True:
                    dp[row][col]=dp[row-1][col]
                elif col >= nums[row]:
                    dp[row][col]= dp[row-1][col-nums[row]]
        return dp[-1][-1]==True
                    
        
        
        
        """   Sum->   
          0 1 2 3 4 5
        0 T T F F F F  # [1]       
        1 T T T T F F  # [1,2]
        2 T T T T T T  # [1,2,3]
        3 T T T T T T  # [1,2,3,4]       """

The above solution has time and space complexity of O(N*S)O(N∗S), where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
