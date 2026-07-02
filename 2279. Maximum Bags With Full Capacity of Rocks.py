class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        new =[]
        for i in range(len(rocks)):
            n= capacity[i] - rocks[i]
            new.append(n)
            
        new.sort()
        for i in range(len(new)):
            if new[i]!=0 and new[i] <=additionalRocks:
                additionalRocks-=new[i]
                new[i] = 0
        res =0
        for i in new:
            if i==0:
                res+=1
        return res
