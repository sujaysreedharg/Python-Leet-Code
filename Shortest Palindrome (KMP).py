class Solution:
    def KMP(self,string):
        substring = string + "#" + string[::-1]
        print(substring)
        pattern =self.findpattern(substring)
        return string[pattern[-1]+1:][::-1]+string
    def findpattern(self,substring):
        j=0
        i=1
        pattern = [-1 for x in substring]
        while i<len(substring):
            if substring[j]==substring[i]:
                pattern[i]=j
                i+=1
                j+=1
            elif j>0:
                j = pattern[j-1]+1
            else:
                i+=1
        return pattern

sol = Solution()
print(sol.KMP("catacb"))









https://leetcode.com/problems/shortest-palindrome/discuss/60113/clean-kmp-solution-with-super-detailed-explanation
