class SuffixTrie:
    def __init__(self,string):
        self.root = {}
        self.endsymbol ="*"
        self.populatesuffixtriefrom(string)
    # O(n^2) Time | O(n^2) Space
    def populatesuffixtriefrom(self,string):
        for i in range(len(string)):
            self.insertstringstartingat(i,string)
    def insertstringstartingat(self,i,string):
        node=self.root
        for j in range(i,len(string)):
            letter= string[j]
            if letter not in node:
                node[letter]={}
                print(node)
            node=node[letter]
            print(node)
        node[self.endsymbol]=True
    # O(m) Time where 'm' is the length of the string to search | O(1)  Space
    def searchsuffix(self,string):
        node=self.root
        for letter in string:
            if letter not in node:
                return False
            node=node[letter]
        return self.endsymbol in node
objectnew= SuffixTrie("babc")

print(objectnew.searchsuffix("bab"))
