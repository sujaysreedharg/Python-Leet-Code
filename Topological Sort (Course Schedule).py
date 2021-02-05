from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedorder=[]
        sources=deque()
        if numCourses==0:
            return False
        indegree={i: 0 for i in range(numCourses)}
        graph={i: [] for i in range(numCourses)}
        for edges in prerequisites:
            parent,child = edges[0],edges[1]
            graph[parent].append(child)
            indegree[child]+=1
        for key in indegree:
            if indegree[key]==0:
                sources.append(key)
        while sources:
            vertex=sources.popleft()
            sortedorder.append(vertex)
            for child in graph[vertex]:
                indegree[child]-=1
                if indegree[child]==0:
                    sources.append(child)
        if len(sortedorder)!=numCourses:
            return False
        print(sortedorder)
        return True
