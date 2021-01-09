class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        if len(nums)>1:
            
            for i in range(0,len(nums)):
                curSum = max(curSum + nums[i],nums[i])
                maxSum = max(maxSum,curSum)
            return maxSum
        return nums[0]
            
  Or: Sliding window approach:
 class Solution:
    def buddyStrings(self, arr, k) -> bool:
        max_sum=0
        old_sum=0
        n=len(arr)
        for i in range(k):
            old_sum += arr[i]
        print(old_sum)
    
        for currval in range(k,n):

            old_sum = old_sum- arr[currval-k] + arr[currval] 
            max_sum = max(max_sum, old_sum)

        return max_sum

Sol= Solution()
print(Sol.buddyStrings([100, 200, 300, 400],2))
    Time complexity reduced from O(n²) to O(n) in sliding window approach.         
     Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0       
