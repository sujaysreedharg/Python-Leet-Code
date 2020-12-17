class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[None]*len(nums)
        left = 0
        right = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                result[i]= nums[left]*nums[left]
                left+=1
            else:
                result[i]=nums[right]*nums[right]
                right-=1
        return result
        
        
        
        linear time complexity -> O(n) 
        
        
        Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
