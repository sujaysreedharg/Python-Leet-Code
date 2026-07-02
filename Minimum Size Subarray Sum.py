class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        shortest = float("inf")
        
        
        sums= left= right = 0
        
        while right < len(nums):
            sums += nums[right]
            
            
            while sums >= target:
                sums-=nums[left]
                curr = right - left+1 
                left+=1
                shortest = min(curr,shortest)
            right+=1
            
                
                
                
        return shortest if shortest!=float("inf") else 0
