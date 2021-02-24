class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def ok(mid):
            cuts, currentsum = 0,0
            for x in nums:
                currentsum+=x
                if currentsum> mid:
                    cuts+=1
                    currentsum = x
            sub= cuts+1
            return sub<=m
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = (low+high)//2
            if not ok(mid):
                low= mid+1
            else:
                high = mid-1
        return low
