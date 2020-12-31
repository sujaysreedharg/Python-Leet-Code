class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        for i in nums:
            output+= [lst + [i] for lst in output]
        return output
        
        
        
  Complexity Analysis

Time complexity: \mathcal{O}(N \times 2^N)O(N×2 
N
 ) to generate all subsets and then copy them into output list.

Space complexity: \mathcal{O}(N \times 2^N)O(N×2 
N
 ). This is exactly the number of solutions for subsets multiplied by the number NN of elements to keep for each subset.
 
 
 
 Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
