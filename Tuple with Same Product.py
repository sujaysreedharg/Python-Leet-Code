class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans=0
        freq={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                key  = nums[i]*nums[j]
                ans+= freq.get(key,0)
                freq[key]=1+ freq.get(key,0)
        return 8*ans
