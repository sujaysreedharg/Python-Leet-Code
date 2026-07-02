from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree ={i: 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}
        sortedarr =[]
        sources= deque()
        
        for edge in prerequisites:
            parent,child = edge[0],edge[1]
            graph[child].append(parent)
            indegree[parent]+=1
        for key in indegree:
            if indegree[key]==0:
                sources.append(key)
        while sources:
            child = sources.popleft()
            sortedarr.append(child)
            for parent in graph[child]:
                indegree[parent]-=1
                if indegree[parent]==0:
                    sources.append(parent)
                    
        return sortedarr if len(sortedarr) == numCourses else []
