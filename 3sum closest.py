class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result =nums[0]+nums[1]+nums[len(nums)-1]
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                cur_sum = nums[i]+nums[left]+nums[right]
                
                if cur_sum > target:
                    right-=1
                else:
                    left+=1
                
                if abs(cur_sum - target) < abs(result-target):
                    result= cur_sum
        return result
