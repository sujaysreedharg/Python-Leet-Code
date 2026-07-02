class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap={
            "2": "abc",
            "3": "def",
            "4" : "ghi",
            '5': "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        res=[]
        def backrack(i,stri):
            if len(stri)== len(digits):
                res.append(stri)
                return
            
            for c in hashmap[digits[i]]:
                backrack(i+1,stri+c)
        
    
        if digits:
            backrack(0,"")
        return res
