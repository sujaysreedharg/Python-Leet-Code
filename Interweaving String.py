class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        if (l1+l2)!=len(s3):
            return False
        
        cache = [[None for i in range(len(s2)+1)] for j in range(len(s1)+1)]
        return self.isvalid(s1,s2,s3,0,0,cache)
    
    def isvalid(self,s1,s2,s3,i,j,cache):
        if cache[i][j] is not None:
            return cache[i][j]
        k=i+j
        if k == len(s3):
            return True
        if i< len(s1) and  s1[i]==s3[k]:
            cache[i][j] = self.isvalid(s1,s2,s3,i+1,j,cache)
            if cache[i][j]:
                return True
        if j<len(s2) and s2[j]==s3[k]:
            cache[i][j]=self.isvalid(s1,s2,s3,i,j+1,cache)
            return cache[i][j]
        cache[i][j]=False
                
        return False
        
        
        
        Time -> O(nm)
        Space -> O(nm)
