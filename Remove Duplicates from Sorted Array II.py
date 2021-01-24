class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        i=len(nums)-1
        while i>0:
            if nums[i]==nums[i-2]:
                j=i-2
                val=nums[i]
                while j>=0 and val==nums[j]:
                    nums.pop(j)
                    j-=1
                i=j
            else:
                i-=1
