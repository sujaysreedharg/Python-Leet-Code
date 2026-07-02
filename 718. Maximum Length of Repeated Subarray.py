class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res=0
        
        
        dp=[[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        
        for row in range(1,len(nums1)+1):
            for col in range(1,len(nums2)+1):
                if nums1[row-1]==nums2[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                    res=max(dp[row][col],res)
        return res
        
        
        
        
