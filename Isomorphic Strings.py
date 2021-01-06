class Solution(object):
    
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        s_lookup = {}
        t_lookup = {}
		
		# Create mapping to/from chars in s and t
        for i in range(len(s)):
            s_lookup[s[i]] = t[i]
            t_lookup[t[i]] = s[i]
        print(s_lookup)
        print(t_lookup)
            
        #Check that they match
        for i in range(len(s)):
            if s_lookup[s[i]] != t[i] or t_lookup[t[i]] != s[i]:
                return False
        
        return True
Sol= Solution()
print(Sol.isIsomorphic("egg","add"))

	Time Complexity: O(A + B) where A and B are letters in s and t respectively
	Space Complexity: O(A + B) where A and B are letters in s and t respectively


Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
