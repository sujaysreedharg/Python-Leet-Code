class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numberofprovinces = 0
        visited = [False]*len(isConnected)
        def dfs(node):
            visited[node]=True
            for neigh in range(len(isConnected)):
                if isConnected[node][neigh] and not visited[neigh]:
                    dfs(neigh)
            
        for start in range(len(isConnected)):
            if not visited[start]:
                numberofprovinces+=1
                dfs(start)
        return numberofprovinces
