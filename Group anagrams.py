class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_index = {}
        for items in strs:
            s = "".join(sorted(items))
            if s not in map_index:
                map_index[s] = [items]  #if sorted vaue not in dict, then add  it as the key
            else:
                map_index[s].append(items)
        result=[]
        for i in map_index.values():
            result.append(i)
        return result
        
        
        
        
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
