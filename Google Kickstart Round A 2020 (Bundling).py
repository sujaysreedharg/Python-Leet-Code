import sys
sys.setrecursionlimit(int(1e6))
class trie:
    def __init__(self):
        self.val ={}
        self.count = "*"
    def insert(self,word):
        curr= self.val
        for x in word:
            curr[x]= curr.get(x,[0,{}])
            curr[x][0]+=1
            curr = curr[x][1]
        curr["*"]=1
def getsol(K,word):
    count = 0
    for x in word:
        if x=="*":
            continue
        [a,b] = word[x]
        if a >=K:
            count += a//K
            count+= getsol(K,b)
    return count
T = int(input())
u=T
while T>0:
    T-=1
    N,K = map(int,input().split())
    Trie = trie()
    for i in range(N):
        Trie.insert(input())
    print("case #{}:{}".format(u-T,getsol(K,Trie.val)))
