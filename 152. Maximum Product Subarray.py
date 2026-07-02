class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prevminprod=nums[0]
        prevmaxprod=nums[0]
        ans=nums[0]
        for n in nums[1:]:
            currmaxprod= max(n,prevminprod*n,prevmaxprod*n)
            currminprod= min(n,prevminprod*n,prevmaxprod*n)
            prevminprod=currminprod
            prevmaxprod=currmaxprod
            ans=max(ans,currmaxprod)
        return ans
        
        
