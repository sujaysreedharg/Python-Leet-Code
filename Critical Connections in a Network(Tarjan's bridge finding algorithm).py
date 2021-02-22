
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        parent =[-1]*n
        disc,low = [-1]*n,[-1]*n
        bridges = []
        adjlist =collections.defaultdict(list)
        #************important********* if edge is undirected then use this method for creating adjacency list
        for edges in connections:
                adjlist[edges[0]].append(edges[1])
                adjlist[edges[1]].append(edges[0])
        def dfs(u,parent,disc,low,time_):
            disc[u]=low[u] = time_
            time_+=1
            for neigh in adjlist[u]:
                if disc[neigh]==-1:
                    parent[neigh]=u
                    dfs(neigh,parent,disc,low,time_)
                    low[u] = min(low[u],low[neigh])
                    if low[neigh]>disc[u]:
                        print([u,neigh])
                        bridges.append([u,neigh])
                elif parent[u]!=neigh:
                    low[u] = min(low[u],disc[neigh])
        time_=0
        for eachnode in range(n):
            if disc[eachnode]==-1:
                dfs(eachnode,parent,disc,low,time_)
        return bridges
