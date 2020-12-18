class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            if (i>0 and nums[i]==nums[i-1]):
                continue
            left = i+1
            right= len(nums)-1
            while left<right:
                total = nums[left]+nums[right]+nums[i]
                if ( total>0):
                    right = right-1
                elif (total<0):
                    left=left+1
                else:
                    result.append([nums[left],nums[right],nums[i]])
                    while(left<right and nums[left]==nums[left+1]):
                        left+=1
                    while(right>left and nums[right]==nums[right-1]):
                        right-=1
                    left+=1
                    right-=1
        return result
        
        
        
        Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
