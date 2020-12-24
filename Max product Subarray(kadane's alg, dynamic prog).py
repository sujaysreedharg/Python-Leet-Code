class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmaxprod= nums[0]
        prevminprod=nums[0]
        prevmaxprod=nums[0]
        ans=nums[0]
        for num in nums[1:]:
            currmaxprod= max(num,prevmaxprod*num,prevminprod*num)
            currminprod= min(num,prevmaxprod*num,prevminprod*num)
            prevmaxprod = currmaxprod
            prevminprod = currminprod
            ans= max(ans,currmaxprod)
        return ans
        
        
        
        
 O(n) -> Time
 O(1) -> Space
 
 Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
