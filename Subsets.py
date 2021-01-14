class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.backtrack(nums,0,[],ans)
        return ans
    def backtrack(self,nums,startidx,cur_list,ans):
        ans.append(cur_list[:])
        n=len(nums)
        for i in range(startidx,n):
            cur_list.append(nums[i])
            
            self.backtrack(nums,i+1,cur_list,ans)
            cur_list.pop()
                
 
 
 Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
