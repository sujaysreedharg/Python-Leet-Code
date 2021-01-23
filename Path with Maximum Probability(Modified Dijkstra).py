class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        if not n or not edges:
            return 0
        graph =collections.defaultdict(list)
        
     
        for i in range(len(edges)):
            k, v = edges[i]
            graph[k].append((v, succProb[i]))
            graph[v].append((k, succProb[i])) 
        print(graph)
        visitedanddist={}
        pq=[(-1,start)]
        while pq:
            dis,node= heapq.heappop(pq)
            dis*=-1
            if node in visitedanddist:
                continue
            visitedanddist[node]=dis
            for neigh,d in graph[node]:
                if neigh not in visitedanddist:
                    heapq.heappush(pq,(-1*(dis*d),neigh))
        print(visitedanddist)
        return visitedanddist[end] if end in visitedanddist else 0
        
        
        
        
Big-O:

Time: O(ElogV), E = edges, V = Verticies
Space: O(V) - all nodes need to be stored - costSoFar dict, adjacencyList
