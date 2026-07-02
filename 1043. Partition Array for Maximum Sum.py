class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1 for _ in range(len(arr))]
        
        def dfs(ind):
            if ind==len(arr):
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            lens=0
            max_val = float("-inf")
            max_ans = float("-inf")
            for i in range(ind,min(ind+k,len(arr))):
                lens+=1
                max_val = max(max_val,arr[i])
                sums = lens*max_val + dfs(i+1)
                max_ans = max(max_ans, sums)

            dp[ind] = max_ans
            return dp[ind]
                
                
                
        
        
        
        return dfs(0)
