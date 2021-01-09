class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p:
            return []
        hashmap={}
        for i in p:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        counter=len(hashmap)
        print(counter)
        begin=0
        end=0
        wordsize=len(p)
        result=[]
        while end<len(s):
            endchar=s[end]
            if endchar in hashmap:
                hashmap[endchar]-=1
                if hashmap[endchar]==0:
                    counter-=1
            end+=1
            while counter==0:
                if end-begin == wordsize:
                    result.append(begin)
                startchar=s[begin]
                if startchar in hashmap:
                    hashmap[startchar]+=1
                    if hashmap[startchar]>=1:
                        counter+=1
                begin+=1
        return result
