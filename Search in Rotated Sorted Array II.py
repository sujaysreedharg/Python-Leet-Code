class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if (None == nums or 0 == len(nums)):
            return 
        left =0 
        n = len(nums)
        right = n-1
        while (left<=right):
            while left <right and nums[left]==nums[right]:
                left+=1
            while left<right and nums[right]==nums[left]:
                right-=1
            mid =(left+right)//2
            if nums[mid]==target:
                return True
            elif  nums[mid]>=nums[left]:
                if target >= nums[left] and target<=nums[mid]:
                    right = mid-1
                else:
                    left=mid+1
            elif nums[mid]<= nums[left]:
                if target >= nums[mid] and target<= nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
        
        
        
Complexity Analysis

Time complexity : O(N) worst case, O(logN) best case, where N is the length of the input array.

Worst case: This happens when all the elements are the same and we search for some different element. At each step, we will only be able to reduce the search space by 1 since arr[mid] equals arr[start] and it's not possible to decide the relative position of target from arr[mid]. Example: [1, 1, 1, 1, 1, 1, 1], target = 2.

Best case: This happens when all the elements are distinct. At each step, we will be able to divide our search space into half just like a normal binary search.

This also answers the following follow-up question:

Would this (having duplicate elements) affect the run-time complexity? How and why?
As we can see, by having duplicate elements in the array, we often miss the opportunity to apply binary search in certain search spaces. Hence, we get O(N) worst case (with duplicates) vs O(logN) best case complexity (without duplicates).

Space complexity : O(1).
