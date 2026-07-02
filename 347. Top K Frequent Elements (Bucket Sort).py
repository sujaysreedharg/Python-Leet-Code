class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countHashmap={}
        freq=[[] for _ in range(len(nums)+1)]
        
        for n in nums:
            countHashmap[n]=1+countHashmap.get(n,0)
        
        for nums,count in countHashmap.items():
            freq[count].append(nums)
            
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for nums in freq[i]:
                res.append(nums)
                if len(res)==k:
                    return res
