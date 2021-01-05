class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        string=""
        self.backtrack(result,string,0,0,n)
        return result
    def backtrack(self,result,currentstring,open,close,max):
        if (len(currentstring)==max*2):
            result.append(currentstring)
            return
        if (open<max):
            self.backtrack(result,currentstring+ "(", open+1,close,max)
        if (close<open):
            self.backtrack(result,currentstring+ ")", open,close+1,max)
            
            
 Time Complexity :  4 ** n /( n* root(n)) Each valid sequence has at most n steps during the backtracking procedure.

Space Complexity :  4 ** n /( n* root(n))

            
            
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
