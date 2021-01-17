class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return  0
        if len(needle)==0:
            return 0
        pattern = self.findpattern(needle)
        return self.doesmatch(haystack,needle,pattern)
    def findpattern(self,needle):
        pattern =[-1 for x in needle]
        j=0
        i=1
        while i<len(needle):
            if needle[j]==needle[i]:
                pattern[i]= j
                i+=1
                j+=1
            elif j>0:
                j = pattern[j-1]+1
            else:
                i+=1
        return pattern
    def doesmatch(self,haystack,needle,pattern):
        i=0
        j=0
        while  i-(j-len(needle)) <= len(haystack):
            if haystack[i]==needle[j]:
                if j==len(needle)-1:
                    return i-j
                i+=1
                j+=1
            elif  j>0:
                j = pattern[j-1]+1
            else:
                i+=1
        return -1
            
Why this algorithm is amazing?
The normal sliding window approach has a Time Complexity of O(n*m) where n= len of haystack & m = len of needle. The KMP algorithm has a Time Complexity of O(n+m) and a Space of O(m).

Why?

KMP avoids recomputation of strings which have a repitition (Pattern).



Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
