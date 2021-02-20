Time -> O(logn)
Space -> O(logn)


V = 4
dsuf  = [[-1,0] for _ in range(V)]
# -1 -> Absolute Parent(Find by Path Compression) and 0 -> Rank (Union)
def cycle(edgelist):
    for pairs in edgelist:
        frompairs= findabsroot(pairs[0])
        topairs= findabsroot(pairs[1])
        if frompairs==topairs:
            return True
        union(frompairs,topairs)
    return False

def findabsroot(node):
    if dsuf[node][0]==-1:
        return node
    dsuf[node][0]= findabsroot(dsuf[node][0])
    return dsuf[node][0]

def union(frompairs,topairs):
    findparentof1 = findabsroot(frompairs)
    findparentof2 = findabsroot(topairs)
    if dsuf[findparentof1][1] > dsuf[findparentof2][1]:
        dsuf[findparentof2][0] = findparentof1
    elif dsuf[findparentof1][1] < dsuf[findparentof2][1]:
        dsuf[findparentof1][0] = findparentof2
    else:
        dsuf[findparentof1][0] = findparentof2
        dsuf[findparentof2][1]+=1

def main():
    edgelist = [[0,1],[0,3],[2,3],[1,2]]
    
    if cycle(edgelist):
        return True
    return False

print(main())
