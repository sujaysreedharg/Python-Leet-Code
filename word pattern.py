class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_index = {}
        word = s.split()
        if len(pattern) !=  len(word):
            return False
        for i in range(len(word)):
            c = pattern[i]
            d = word[i]
            char_key = "char_{}".format(c)
            char_value = "word_{}".format(d)
            if char_key not in map_index:
                map_index[char_key] = i
            if char_value not in map_index:
                map_index[char_value] = i
            if map_index[char_key]!= map_index[char_value]:
                return False
        return True





Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
test case : "abba"
"dog cat cat dog"
 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
