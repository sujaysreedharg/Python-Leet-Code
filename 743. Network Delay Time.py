class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph=collections.defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1],time[2]))
        pq=[(0,K)]
        visitedanddist={}
        while pq:
            dist,node=heapq.heappop(pq)
            if node in visitedanddist:
                continue
            visitedanddist[node]=dist
            for neigh,d in graph[node]:
                if neigh in visitedanddist:
                    continue
                heapq.heappush(pq,(dist+d,neigh))
        return max(visitedanddist.values()) if len(visitedanddist)==N else -1
            
