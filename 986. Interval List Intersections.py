class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res=[]
        aptr=0
        bptr=0
        
        while aptr< len(firstList) and bptr < len(secondList):
            temp=[0,0]
            if firstList[aptr][0]<=secondList[bptr][1] and firstList[aptr][1]>=secondList[bptr][0]:
                temp[0] = max(firstList[aptr][0],secondList[bptr][0])
                temp[1] = min(firstList[aptr][1],secondList[bptr][1])
                res.append(temp)
            if firstList[aptr][1] > secondList[bptr][1]:
                bptr+=1
            else:
                aptr+=1
        return res
                
