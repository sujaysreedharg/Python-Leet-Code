class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        hashmap={}
        for i in s1:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        wordsize =len(s1)
        end=0
        counter=len(hashmap)
        print(counter)
        begin=0
        while end<len(s2):
            endchar=s2[end]
            if endchar in hashmap:
                hashmap[endchar]-=1
                if hashmap[endchar]==0:
                    counter-=1
            end+=1
            while counter==0:
                print(begin,end)
                print(wordsize)
                if (end-begin) == wordsize:
                    return True
                startchar=s2[begin]
                if startchar in hashmap:
                    hashmap[startchar]+=1
                    if hashmap[startchar]>=1:
                        counter+=1
                begin+=1
        return False
