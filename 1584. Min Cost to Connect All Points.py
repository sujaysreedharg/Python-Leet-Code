class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N=len(points)
        graph={i: [] for i in range(N)}
        
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                graph[i].append([cost,j])
                graph[j].append([cost,i])
        res=0
        q= [[0,0]]
        visited=set()
        while len(visited) < N:
            neicosts,neis = heapq.heappop(q)
            if neis in visited:
                continue
            res+=neicosts
            visited.add(neis)
            
            for neicost,nei in graph[neis]:
                if nei not in visited:
                    heapq.heappush(q,[neicost,nei])
        return res
            
                
        
