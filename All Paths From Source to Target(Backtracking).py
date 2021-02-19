class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graphrep= collections.defaultdict(list)
        for source in range(len(graph)):
            if source not in graphrep:
                graphrep[source].extend(graph[source])
            else:
                graphrep[source].extend(graph[source])
        print(graphrep)
        result =[]        

        def dfsbacktrack(node,currentresult):
            print(node)
            currentresult.append(node)
            print(currentresult)
            if node== len(graph)-1:
                return result.append(currentresult)
                
            print(node,graphrep[node])
            for neigh in graphrep[node]:
                dfsbacktrack(neigh,currentresult[::])
            currentresult.pop()   
            
        for edges in graphrep[0]:
            dfsbacktrack(edges,[0])
        return result
