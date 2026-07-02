class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]
        
        
        
        def backtrack(openB,closeB):
            
            if openB == closeB == n:
                res.append("".join(stack))
                return
            if openB < n:
                stack.append("(")
                backtrack(openB+1,closeB)
                stack.pop()
            if openB > closeB:
                stack.append(")")
                backtrack(openB,closeB+1)
                stack.pop()
        
        backtrack(0,0)
        
        return res
        
