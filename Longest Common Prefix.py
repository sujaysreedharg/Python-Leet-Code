class trie:
    def __init__(self):
        self.root ={}
        self.endsymbol = "*"
    def insert(self,word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] ={}
            node= node[c]
            
        node[self.endsymbol] = True
    def printtrie(self):
        node= self.root
        ans=[]
        while node!=None and self.endsymbol not in node and len(node.values())==1:
            ans.append([i for i in node])
            print(node.values())
            for c in node:
                node=node[c]
        res=""
        for i in ans:
            for j in i:
                res+=j
        print(res)
                
Trie = trie()
Trie.insert("flower")
Trie.insert("flow")
Trie.insert("flight")
Trie.printtrie()
