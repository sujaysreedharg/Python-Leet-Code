class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def checkbip(node,graph_,n,color):
            color[node]=1
            queue=[node]
            while queue:
                curr= queue.pop(0)
                # print(curr)
                for nei in graph_[curr]:
                    if color[nei]==color[curr]:
                        return False
                    if color[nei]==-1:

                        queue.append(nei)
                        color[nei] = 1 - color[curr]

            return True
        
        color =[-1 for _ in range(len(graph))]
        graph_ = defaultdict(list)
        for i in range(len(graph)):
            graph_[i].extend(graph[i])
        for i in range(len(graph_)):
            # print(i)
            if color[i]==-1:
                if not checkbip(i,graph_,len(graph),color):
                    return False
        return True
