class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        psum=[0]*len(nums)
        ssum=[0]*len(nums)
        
        start=nums[0]
        end=nums[-1]
        
        for i in range(1,len(nums)):
            psum[i]=start 
            start+=nums[i]
            
        for j in range(len(nums)-2,-1,-1):
            ssum[j]=end 
            end+=nums[j]
        for i in range(len(nums)):
            if psum[i]==ssum[i]:
                return i
        return -1 
