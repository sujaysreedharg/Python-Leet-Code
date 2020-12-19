class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset= set()
        aptr =0
        bptr=0
        maxval=0
        while bptr < len(s):
            if s[bptr] not in hashset:
                hashset.add(s[bptr])
                bptr+=1
                maxval=max(maxval,len(hashset))
            else:
                hashset.remove(s[aptr])
                aptr+=1
            

        return maxval
        
        
        
        
        
        Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
