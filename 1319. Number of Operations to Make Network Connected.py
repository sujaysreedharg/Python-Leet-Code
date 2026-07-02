class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        cables=len(connections)
        if cables < n-1:
            return -1
        adj=collections.defaultdict(list)
        for edges in connections:
            adj[edges[0]].append(edges[1])
            adj[edges[1]].append(edges[0])    
        visited=set()
        ans=0
        def dfs(node):
            visited.add(node)
            for child in adj[node]:
                if child not in visited:
                    dfs(child)
        for i in range(n):
            if i not in visited:
                ans+=1
                dfs(i)
        return ans-1

            
        
