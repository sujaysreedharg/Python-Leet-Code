class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for edge in flights:
            if edge[0] not in graph:
                graph[edge[0]].append((edge[1],edge[2]))
            else:
                graph[edge[0]].append((edge[1],edge[2]))
        print(graph)
        pq = [(0,-1,src)]
        while pq:
            cost,steps,currdestination  = heapq.heappop(pq)
            if steps>K:
                continue
            if currdestination == dst:
                return cost
            for neigh,neighcost in graph[currdestination]:
                heapq.heappush(pq,(cost+neighcost,steps+1,neigh))
        return -1
            
