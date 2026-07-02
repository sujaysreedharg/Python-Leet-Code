class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        stack=["JFK"]
        res=[]
        
        graph = collections.defaultdict(list)
        
        for edge in tickets:
            heapq.heappush(graph[edge[0]],edge[1])
        
        while stack:
            origin = stack[-1]
            
            if not graph[origin]:
                res.append(origin)
                stack.pop()
            else:
                dest = heapq.heappop(graph[origin])
                stack.append(dest)
        return res[::-1]
