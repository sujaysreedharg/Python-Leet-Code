class Solution:
    def countVowelStrings(self, n: int) -> int:
        result=[1,1,1,1,1]
        for i in range(n):
            for k in range(5):
                result[k]=sum(result[k:])
                
        return result[0]
