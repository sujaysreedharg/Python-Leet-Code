class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i=0
        result=[]
        for j in range(len(s)):
            if j==len(s)-1 or s[j]!=s[j+1]:
                if  (j-i+1>=3):
                    result.append([i,j])
                i=j+1
        return result
        
        
        
        
//time O(N)
//space O(1)
