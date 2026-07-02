class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap ={}
        for i in nums:
            hashmap[i]= 1+ hashmap.get(i,0)
        for key,value in hashmap.items():
            if value > (len(nums)//2):
                return key
        
