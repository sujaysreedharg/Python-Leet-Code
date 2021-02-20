class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1,p2: abs(p1[0]- p2[0]) + abs(p1[1]-p2[1])
        c= collections.defaultdict(list)
        n=len(points)
        for i in range(n):
            for j in range(i+1,n):
                d  = manhattan(points[i],points[j])
                c[i].append((d,j))
                c[j].append((d,i))
        cnt,visited, ans, heap = 0,[0]*n,0, c[0]
        visited[0] =1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if visited[j]!=1:
                visited[j],cnt,ans = 1,cnt+1,ans+d
                for adjneigh in c[j]:
                    heapq.heappush(heap,adjneigh)
            if cnt>=n:
                break
        return ans
