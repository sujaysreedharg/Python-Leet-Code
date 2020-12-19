class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charactercount = [0]*26 
        n = len(s)
        startptr = 0
        endptr = 0
        maxlength = 0 
        maxcount = 0
        while( endptr<n):
            charactercount[ord(s[endptr])-ord('A')]+=1
            maxcount = max(maxcount, charactercount[ord(s[endptr])-ord('A')])
            while ( endptr -startptr - maxcount + 1) > k:
                charactercount[ord(s[startptr])-ord('A')]-=1
                startptr+=1
            maxlength = max(maxlength, endptr-startptr+1)
            endptr+=1
        return maxlength
        
        
        
        
        Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
