class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        result =[None,None]
        totalwidth=0
        lines=1
        for i in s:
            charwidth = widths[ord(i)-ord('a')]
            totalwidth+=charwidth
            if totalwidth>100:
                lines+=1
                totalwidth=charwidth
        result[0]=lines
        result[1]=totalwidth
        return result
        
        
        
 Time Complexity: O(S.length), as we iterate through S.

Space Complexity: O(1) additional space, as we only use lines and width. 
