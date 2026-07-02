class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashmap1 ={}
        hashmap2={}
        for i in s:
            hashmap1[i] = 1 + hashmap1.get(i,0)
        for j in t:
            hashmap2[j] = 1 + hashmap2.get(j,0)
        for k,v in hashmap2.items():
            if k in hashmap1:
                while hashmap1[k] > 0 and v > 0:
                    hashmap1[k]-=1
                    v-=1
        return sum(hashmap1.values())
        
