# Single Traversal Algorithm -> O(V+E) -> Time

maturegraph = [[0,1],[1,0],[0,3],[3,0],[0,2],[2,0],[1,2],[2,1],[3,4],[4,3]]
import collections
V= 5
graph = collections.defaultdict(list)
for edges in maturegraph:
    if edges[0] not in graph:
        graph[edges[0]].append(edges[1])
    else:
        graph[edges[0]].append(edges[1])
print(graph)
disc,low = [-1 for _ in range(V)],[-1 for _ in range(V)]
print(disc,low)
parent = [-1]*V
art_pt= [False]*(V)
time_=0


def dfs(u,disc,low,parent,time_,art_pt):
    disc[u]=low[u] = time_
    time_+=1
    child=0
    for neigh in graph[u]:
        if disc[neigh]==-1:
            parent[neigh]= u
            child+=1
            dfs(neigh,disc,low,parent,time_,art_pt)
            low[u]= min(low[u],low[neigh])
            if parent[u]==-1 and child>1:
                art_pt[u]=True
            if parent[u]!=-1 and low[neigh]>= disc[u]:
                art_pt[u]=True
        elif neigh!= parent[u]:
            low[u]= min(low[u],disc[neigh])

for i in range(V):
    if disc[i]==-1:
        dfs(i,disc,low,parent,time_,art_pt)
print(art_pt)
