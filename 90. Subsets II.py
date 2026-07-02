class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        
        
        def backtrack(i,array):
            if i==len(nums):
                res.append(array.copy())
                return
            array.append(nums[i])
            backtrack(i+1,array)
            array.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,array)
        backtrack(0,[])    
        return res
