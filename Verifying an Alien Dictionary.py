class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        
        letter = {}
        for i in range(len(order)):
            letter[order[i]]= i
        def ismatch(word1,word2):
            found = False
            n= len(word1)
            m =len(word2)
            for i in range(min(n,m)):
                if word1[i]!= word2[i]:
                    if letter[word1[i]] > letter[word2[i]]:
                        return False
                    found = True
                    break
            if found == False and n>m:
                return False
            return True
        for i in range(1,len(words)):
            result=ismatch(words[i-1],words[i])
            if result == False:
                return False
        return True
                    
