class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap={}
        res=0
        for i in nums:
            hashmap[i] = 1+ hashmap.get(i,0)
        for i in hashmap:
            if k==0 and  hashmap[i]>=2:
                res+=1
            elif k!=0 and i+k in hashmap:
                res+=1
        return res
