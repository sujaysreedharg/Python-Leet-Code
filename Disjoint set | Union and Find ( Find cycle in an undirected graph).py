Time -> O(n)
Space -> O(n)


V = 4
dsuf  = [-1 for _ in range(V)]
def cycle(edgelist):
    for pairs in edgelist:
        frompairs= findabsroot(pairs[0])
        topairs= findabsroot(pairs[1])
        if frompairs==topairs:
            return True
        union(frompairs,topairs)
    return False

def findabsroot(node):
    if dsuf[node]==-1:
        return node
    return findabsroot(dsuf[node])

def union(frompairs,topairs):
    findparentof1 = findabsroot(frompairs)
    findparentof2 = findabsroot(topairs)
    dsuf[findparentof1]= findparentof2

def main():
    edgelist = [[0,1],[0,3],[2,3],[1,2]]
    
    if cycle(edgelist):
        return True
    return False

print(main())
