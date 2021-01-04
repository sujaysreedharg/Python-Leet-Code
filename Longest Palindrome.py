class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs=0
        unpaired=set()
        for char in s:
            if char not  in unpaired:
                unpaired.add(char)
            else:
                
                pairs+=1
                unpaired.remove(char)
        return pairs*2+1 if unpaired else pairs*2
        
        
    Time Complexity: O(N) where N is the length of s. We need to count each letter.

Space Complexity: O(1) the space for our count, as the alphabet size of s is fixed. We should also consider that in a bit complexity model, technically we need)O(logN) bits to store the count values.    
        
        
        
        
        Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
