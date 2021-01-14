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
                
 
 [1,2,3]					         []  	                                     [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
				         /            \         	\
				 0,1   [1]         1,0  [2]       2,0   [3]
				    /    \         	    \ 
			 1,1 [1,2]   1,2  [1,3]   2,2  [2,3]
				/     
			2,2  [1,2,3]    
    
    
    [[]]
i,startidx 0 0
beforbacktrack [1]
[[], [1]]
i,startidx 1 1
beforbacktrack [1, 2]
[[], [1], [1, 2]]
[[]]
i,startidx 0 0
beforbacktrack,nums[i] [1] 1
[[], [1]]
i,startidx 1 1
beforbacktrack,nums[i] [1, 2] 2
[[], [1], [1, 2]]
[[]]
i,startidx, nums[i] 0 1
beforbacktrack,nums[i] [1] 1
[[], [1]]
i,startidx, nums[i] 1 2
beforbacktrack,nums[i] [1, 2] 2
[[], [1], [1, 2]]
[[]]
i,startidx, nums[i] 0 0 1
beforbacktrack,nums[i] [1] 1
[[], [1]]
i,startidx, nums[i] 1 1 2
beforbacktrack,nums[i] [1, 2] 2
[[], [1], [1, 2]]
[[]]
i,startidx, nums[i] 0 0 1
[[]]
i,startidx, nums[i] 0 0 1
beforbacktrack,nums[i] [1] 1
[[], [1]]
i,startidx, nums[i] 1 1 2
beforbacktrack,nums[i] [1, 2] 2
[[], [1], [1, 2]]
[[]]
i,startidx, nums[i] 0 0 [1]
beforbacktrack,nums[i] [1] 1
[[], [1]]
i,startidx, nums[i] 1 1 [2]
beforbacktrack,nums[i] [1, 2] 2
[[], [1], [1, 2]]
[[]]
i,startidx, nums[i] 0 0 [1]
beforbacktrack,nums[i] [1] 1
[[], [1]]
i,startidx, nums[i] 1 1 [2]
beforbacktrack,nums[i] [1, 2] 2
[[], [1], [1, 2]]
i,startidx, nums[i] 2 2 [3]
beforbacktrack,nums[i] [1, 2, 3] 3
[[], [1], [1, 2], [1, 2, 3]]
afterbacktrack [1, 2]
afterbacktrack [1]
i,startidx, nums[i] 2 1 [3]
beforbacktrack,nums[i] [1, 3] 3
[[], [1], [1, 2], [1, 2, 3], [1, 3]]
afterbacktrack [1]
afterbacktrack []
i,startidx, nums[i] 1 0 [2]
beforbacktrack,nums[i] [2] 2
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2]]
i,startidx, nums[i] 2 2 [3]
beforbacktrack,nums[i] [2, 3] 3
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3]]
afterbacktrack [2]
afterbacktrack []
i,startidx, nums[i] 2 0 [3]
beforbacktrack,nums[i] [3] 3
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
afterbacktrack []
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    
    
 Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
