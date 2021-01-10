class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        elif len(nums)==1:
            return False
        hashtable = set()
        for i in range(0,len(nums)):
            if nums[i] not in hashtable:
                hashtable.add(nums[i])
            elif nums[i] in hashtable:
                return True
                
                
                
                
      Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true









Time complexity : O(n)O(n). We do search() and insert() for nn times and each operation takes constant time.

Space complexity : O(n)O(n). The space used by a hash table is linear with the number of elements in it.
