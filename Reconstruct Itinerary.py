import heapq as heap
import collections
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
graph2 = collections.defaultdict(list)
for edges in tickets:
    if edges[0] not in graph2:
        heap.heappush(graph2[edges[0]],edges[1])
    else:
        heap.heappush(graph2[edges[0]],edges[1])
print(graph2)
stack  = ["JFK"]
result =[]
while stack:
    origin  = stack[-1]
    if not graph2[origin]:
        result.append(origin)
        stack.pop()
    else:
        dest= heap.heappop(graph2[origin])
        stack.append(dest)
print(result[::-1])
