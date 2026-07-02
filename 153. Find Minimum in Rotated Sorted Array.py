class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right = len(nums)-1
        if len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        while left<=right:
            mid=(left+right)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] >=nums[left] and nums[mid] > nums[right]:
                left=mid+1
            else:
                right=mid-1
        return nums[left]
