class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq=[]
        maps={'a':a,'b': b,'c': c}
        for i in maps:
            if maps[i]!=0:
                heapq.heappush(pq,[-maps[i],i])
        
        res=[]
        while pq:
            cnt,ltr=heapq.heappop(pq)
            if len(res)>1 and res[-1]==res[-2]==ltr:
                if not pq:
                    break
                cnt2,char2= heapq.heappop(pq)
                res.append(char2)
                cnt2+=1
                if cnt2:
                    heapq.heappush(pq,[cnt2,char2])
            else:
                res.append(ltr)
                cnt+=1
            if cnt:
                heapq.heappush(pq,[cnt,ltr])

        return "".join(res)
                
