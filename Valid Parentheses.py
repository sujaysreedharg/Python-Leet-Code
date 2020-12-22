class Solution:
    def isValid(self, s: str) -> bool:
        def peek_stack(value):
            if stack:
                return stack[-1]
            else: return None
        stack=[]
        set=('(', '[','{')
        for i in range(0, len(s)):
            string= s[i]
            if string in  set:
                stack.append(string)
            elif len(stack)!=0 and peek_stack(stack)=='(' and string == ')':
                stack.pop()
            elif len(stack)!=0 and peek_stack(stack)=='[' and string == ']':
                stack.pop()
            elif len(stack)!=0 and peek_stack(stack)=='{' and string == '}':
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
      
      
      
      
      
      Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
