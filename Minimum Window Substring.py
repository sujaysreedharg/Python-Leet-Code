class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap={}
        for i in t:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        begin=0
        end=0
        minword=""
        minwindowsize=float("inf")
        counter=len(hashmap)
        print(counter)
        while end<len(s):
            
            #IndexError: string index out of raange in if s[j] in t: if not end<len(s) in next while loop
            while end<len(s) and counter!=0:
                endchar=s[end]
                if endchar in hashmap:
                    hashmap[endchar]-=1
                    if hashmap[endchar]==0:
                        counter-=1
                end+=1
            while counter==0:
                if end-begin < minwindowsize:
                    minword = s[begin:end]
                    minwindowsize = end-begin
                startchar=s[begin]
                if startchar in hashmap:
                    hashmap[startchar]+=1
                    if hashmap[startchar]>=1:
                        counter+=1
                begin+=1
        return minword
        
        Time -> (s+t)
        Space -> (s+t)
        
        
        https://medium.com/leetcode-patterns/leetcode-pattern-2-sliding-windows-for-strings-e19af105316b
