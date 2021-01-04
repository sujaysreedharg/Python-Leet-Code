class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrack(start,currentlist):
            if start==len(s):
                result.append(currentlist)
            for end in range(start,len(s)):
                if s[start:end]==s[start:end][::-1]:
                    backtrack(end+1,currentlist + [s[start:end+1]])
        result=[]
        backtrack(0,[])
        return result
        
        
        
        
        Time -> O(n* 2^n)
        Space -> O(n)
        
        
        Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
