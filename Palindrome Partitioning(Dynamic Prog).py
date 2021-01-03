class Solution:
    def minCut(self, string: str) -> int:
        palindromes = [[False for i in string] for j in string]
        for i in range(len(string)):
            palindromes[i][i]= True
        for length in range(2, len(string)+1):
            for i in range(0, len(string)-length +1):
                j = i+length-1
                if length==2:
                    palindromes[i][j]= string[i]==string[j]
                else:
                    palindromes[i][j]= string[i] == string[j] and palindromes[i+1][j-1]
            
        cuts  = [None for i in string]
        for i in range(len(string)):
            if palindromes[0][i]:
                cuts[i]=0
            else:
                cuts[i]=cuts[i-1]+1
                for j in range(1,i+1):
                    if palindromes[j][i] and cuts[j-1]+1 < cuts[i]:
                        cuts[i]=cuts[j-1]+1
        return cuts[-1]
    
    
    
    Time -> O(n^2)
    Space -> O(n^2)
    
    
    Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
    
