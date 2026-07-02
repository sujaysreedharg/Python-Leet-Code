class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalin(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        res=[]
        def backtrack(ind,path):
            if ind==len(s):
                res.append(path[:])
                return
            for i in range(ind,len(s)):
                if ispalin(ind,i):
                    path.append(s[ind: i+1])
                    backtrack(i+1,path)
                    path.pop()
        backtrack(0,[])
        return res
