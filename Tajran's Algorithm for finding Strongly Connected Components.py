# Single Traversal Algorithm -> O(V+E) -> Time

maturegraph = [[0,1],[1,2],[1,3],[3,4],[4,0],[4,5],[4,6],[5,6],[6,5]]
import collections
V= 7
graph = collections.defaultdict(list)
for edges in maturegraph:
    if edges[0] not in graph:
        graph[edges[0]].append(edges[1])
    else:
        graph[edges[0]].append(edges[1])
print(graph)
disc,low = [-1 for _ in range(V)],[-1 for _ in range(V)]
print(disc,low)
presentstack = [False]*V
print(presentstack)  #prevents crossedge
mystack =[]
def dfs(i,disc,low,mystack,presentstack,time_):
    disc[i] = low[i]  = time_
    time_+=1
    mystack.append(i)
    presentstack[i] = True
    for neigh in graph[i]:
        if disc[neigh]==-1:
            dfs(neigh,disc,low,mystack,presentstack,time_)
            low[i] = min(low[i],low[neigh])
        else:
            if presentstack[neigh]:
                low[i] = min(low[i],disc[neigh])
    if disc[i]==low[i]:
        while mystack[-1]!=i:
            print("SCC is")
            presentstack[-1] = False
            popped= mystack.pop()
            print(popped)
        presentstack[-1] = False
        popped= mystack.pop()
        print("head of SCC is",popped)

time_ =0
for i in range(V):
    if disc[i]==-1:
        dfs(i,disc,low,mystack,presentstack,time_)
