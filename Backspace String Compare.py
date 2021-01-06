class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        Sstack=[]
        Tstack=[]
        for i in S:
            if Sstack and i =="#":
                Sstack.pop()
                
            
            if i!="#":
                Sstack.append(i) 
        
                    
        for j in T:
            if Tstack and j == "#":
                Tstack.pop()
                
            
            if j!="#":
                Tstack.append(j) 
        
        
        return Sstack==Tstack
        
        
        
        Time -> O(m+n)
        Space -> O(m+n)
        
 Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b
