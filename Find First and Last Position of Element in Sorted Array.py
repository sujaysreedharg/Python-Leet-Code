class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result =[None]*2
        result[0]= self.findstartingindex(nums,target)
        result[1]= self.findendingindex(nums,target)
        return result
    def findstartingindex(self,nums,target):
        index=-1
        start =0
        end= len(nums)-1
        while start<=end:
            mid = (start+end)//2
            if nums[mid]>=target:
                end = mid-1
            else:
                start = mid+1
            if nums[mid]==target:
                index= mid
                
            
        return index
    def findendingindex(self,nums,target):
        index=-1
        start=0
        end = len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]<=target:
                start=mid+1
            else:
                end=mid-1
            if nums[mid]==target:
                index=mid
        return index
        
        
        
        Time -> log(n)
        Space -> O(1)
        
        Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
