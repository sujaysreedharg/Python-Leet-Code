    def canPartition(self, nums: List[int]) -> bool:
        maxes= [x for i in nums]
        leftmax=0
        for i in range(len(nums)):
            height = nums[i]
            maxes[i]= leftmax
            leftmax = max(leftmax, height)
        rightmax= 0 
        for i in reversed(range(len(nums))):
            height= nums[i]
            minheight = min(rightmax,maxes[i])
            if height < minheight:
                maxes[i]= height - minheight
            else:
                maxes[i]=0
            rightmax= max(rightmax,height)
        return sum(maxes)
        
        O(n) -> Time
        O(n) -> Space
        
  
  
  
  Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
