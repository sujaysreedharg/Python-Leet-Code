class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N= len(nums)
        outputarr = [None]*N
        outputarr[0]=1
        for i in range(1,N):
            outputarr[i]=outputarr[i-1]*nums[i-1]
        R=1
        for i in range(N-1,-1,-1):
            outputarr[i]=outputarr[i]*R
            R*=nums[i]
        return outputarr
        
        
        
 O(n) -> Time
 O(1) -> Space
 
 
 Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
