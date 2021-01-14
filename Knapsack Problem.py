class Solution:
    def knapsack(self,items,capacity):
        knapsackvalues=[[0 for i in range(capacity+1)]for j in range(len(items)+1)]
        for row in range(1,len(items)+1):
            currentvalue = items[row-1][0]
            currentweight = items[row-1][1]
            for c in range(0,capacity+1):
                if currentweight > c:
                    knapsackvalues[row][c]= knapsackvalues[row-1][c]
                else:
                    knapsackvalues[row][c] =max(knapsackvalues[row-1][c], knapsackvalues[row-1][c-currentweight]+currentvalue)
        return [knapsackvalues[-1][-1], self.gettheknapsackitems(knapsackvalues,items)]
    def gettheknapsackitems(self,knapsackvalues,items):
        sequence=[]
        row = len(knapsackvalues)-1
        c = len(knapsackvalues[0])-1
        while row>0:
            if knapsackvalues[row][c]==knapsackvalues[row-1][c]:
                row-=1
            else:
                sequence.append(items[row-1])
                
                c-= items[row-1][1]
                row-=1
            if c==0:
                break
        return list(reversed(sequence))
sol=Solution()
print(sol.knapsack([[1,2],[4,3],[5,6],[6,7]],10))

Time  -> O(Nc) where N is the number of items and c is the capacity
Space -> O(Nc) where N is the number of items and c is the capacity
