O(w*nlogn) Time | O(wn) Space
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in hashmap:
                hashmap[sortedWord].append(word)
            else:
                hashmap[sortedWord]=[word]
        return list(hashmap.values())
            
