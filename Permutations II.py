class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=set()
        self.helper(nums,0,result)
        return [list(result) for result in result]
    def helper(self,nums,i,result):
        if i==len(nums)-1:
            result.add(tuple(nums[:]))
            print(result)
        
        for j in range(i,len(nums)):
            self.swap(nums,i,j)
            self.helper(nums,i+1,result)
            self.swap(nums,i,j)
    def swap(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]
