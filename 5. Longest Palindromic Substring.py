O(n^2) Time | O(1) Space
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getPalin(start,end):
            while start>=0 and end<len(s):
                if s[start]!=s[end]:
                    break
                else:
                    start-=1
                    end+=1
            return [start+1,end]
                      
        currentLongest=[0,1]
        for i in range(len(s)):
            even=getPalin(i,i+1)
            odd=getPalin(i,i+2)
            longest=max(odd,even,key= lambda s: s[1]-s[0])
            currentLongest=max(currentLongest,longest,key=lambda s: s[1]-s[0])
        return s[currentLongest[0]:currentLongest[1]]
        
        

            
        
        
        
        
