O(n^2) Time Dijkstra using hashmap

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for edges in times:
            if edges[0] not in graph:
                graph[edges[0]]=[(edges[1],edges[2])]
            else:
                graph[edges[0]].append((edges[1],edges[2]))

        dist={node: float("inf") for node in range(1,N+1)}
        dist[K]=0
        seen = [False]*(N+1)
        while True:
            cand_node = -1
            cand_dist = float("inf")
            for i in range(1,N+1):
                if not seen[i] and dist[i]<cand_dist:
                    cand_node = i
                    cand_dist = dist[i]
            if cand_node<0:
                break
            seen[cand_node]=True
            for neigh,dis in graph[cand_node]:
                dist[neigh]=min(dist[neigh],dist[cand_node]+dis)
        ans=max(dist.values())
        return ans if ans<float("inf") else -1

    
    
    Time-> O(Elog(E)) Space -> O(N+E)   -> Adjacency list and priority queue  (Min heap) Solution:
    
     
    class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for edges in times:
            if edges[0] not in graph:
                graph[edges[0]]=[(edges[1],edges[2])]
            else:
                graph[edges[0]].append((edges[1],edges[2]))

        visitedanddist={}
        pq=[(0,K)]
        while pq:
            dis,node= heapq.heappop(pq)
            if node in visitedanddist:
                continue
            visitedanddist[node]=dis
            for neigh,d in graph[node]:
                if neigh not in visitedanddist:
                    heapq.heappush(pq,(dis+d,neigh))
        return max(visitedanddist.values()) if len(visitedanddist)==N else -1
