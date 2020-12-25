class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        hashmap={}
        lower=paragraph.lower()
        text = re.split('\W+',lower)
        bannedlist = set(banned)
        mostcommonword=""
        for words in text:
            if words in bannedlist:
                continue
            if words not in hashmap:
                hashmap[words]=1
            elif words in hashmap:
                hashmap[words]+=1
        maxword=0
        for keys,values in hashmap.items():
            if values > maxword:
                maxword = values
                mostcommonword =keys
        return mostcommonword
        
        
        O(n) -> Time
        O(n) -> Space
        
        
        Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.

 

Example:

Input: 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
        
