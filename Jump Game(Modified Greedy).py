class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        furthestreached=0
        while i<=furthestreached and furthestreached <len(nums)-1:
            furthestreached = max(furthestreached,nums[i]+i)
            i+=1
        return furthestreached>=len(nums)-1
