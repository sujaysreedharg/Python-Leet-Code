class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap=Counter(s)
        maxheap = [[-count,string] for string,count in hashmap.items()]
        heapq.heapify(maxheap)
        prev=None
        res=""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            
            count,string = heapq.heappop(maxheap)
            count+=1
            res+=string
            
            if prev:
                heapq.heappush(maxheap,prev)
                prev=None
            if count!=0:
                prev = [count,string]
        return res
                
        
