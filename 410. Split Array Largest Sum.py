class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r= sum(nums)
        def cansplit(largest):
            sub=1
            currSum=0
            for i in nums:
                currSum+= i
                if currSum >largest:
                    sub+=1
                    currSum=i
            return sub <=k   
        res=r
        while l<=r:
            mid = (l+r)//2
            if cansplit(mid):
                res=mid
                r= mid-1
            else:
                l=mid+1
        return res 
        
                
