class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxareaofwater =0
        while i<j:
            currentareaofwater = (j-i)*min(height[i],height[j])
            maxareaofwater = max(currentareaofwater,maxareaofwater)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1
        return maxareaofwater
        
        
        
        
        
        
        Time -> O(n)
        Space -> O(1)
        
        
        https://leetcode.com/problems/container-with-most-water/solution/
