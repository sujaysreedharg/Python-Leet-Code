class Solution:
    def __init__(self):
        self.res=[]
    
    def permute(self, nums):
        self.dfsbacktrack(nums,[])
        return self.res
    def dfsbacktrack(self,nums,path):
        if not nums:
            self.res.append(path)
        for x in range(len(nums)):
            print('nums',nums)
            self.dfsbacktrack(nums[:x]+nums[x+1:],path+[nums[x]])

            
sol=Solution()
print(sol.permute([1,2,3]))



















class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations=[]
        self.permutationshelp(0,nums,permutations)
        return permutations
    def permutationshelp(self,i,nums,permutations):
        if i == len(nums)-1:
            permutations.append(nums[:])
            #i comes to the last element and takes a snap shot and then j gets incremented and now its gonna be swapped
            #second loop takes the snap shot and then gonna be swapped
        else:
            for j in range(i,len(nums)):
                #[1,2,3]
                self.swap(nums,i,j)
                #no swap for firstloop
                #second loop [1,3,2]
                self.permutationshelp(i+1,nums,permutations)
                #again no swap till i comes to the last element
                self.swap(nums,i,j)
                #swap back to [1,2,3]
    def swap(self,nums,i,j):
        nums[i],nums[j]=nums[j],nums[i]
        
        
        
        
        
        
        
        
        
    O(n* n!) -> Time
    O(n* n!) -> Space
    
    
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
