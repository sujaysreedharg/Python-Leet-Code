class Solution:
    def countSubstrings(self, s: str) -> int:
        def getPalin(start,end):
            result=0
            while start>=0 and end<len(s):
                if s[start]!=s[end]:
                    break
                else:
                    result+=1
                    start-=1
                    end+=1
            return result
        count=0         
        for i in range(len(s)):
            count+=1+getPalin(i,i+1)+getPalin(i,i+2)
            
        return count
        
