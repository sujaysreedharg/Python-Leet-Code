class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_index = {}
        for i in range(len(s)):
            c = s[i]
            if c not in map_index:
                map_index[c]= 1
            else:
                map_index[c]+=1
        for j in range(len(t)):
            d= t[j]
            if d not in map_index:
                return False
            if map_index[d] < 1:
                return False
            map_index[d]-=1
        return True
            
                
                
        
        
        Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
