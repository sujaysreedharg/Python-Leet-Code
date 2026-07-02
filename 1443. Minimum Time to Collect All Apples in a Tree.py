import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph=collections.defaultdict(list)
        for nodes in edges:
            graph[nodes[0]].append(nodes[1])
            graph[nodes[1]].append(nodes[0])
        visited=set()
        print(graph)
        def dfs(node):
            if node in visited:
                return 0
            secs=0
            visited.add(node)
            for child in graph[node]:
                secs+=dfs(child)
            if secs>0:
                return secs+2
            return 2 if hasApple[node] else 0
        return max(dfs(0)-2,0)
                
