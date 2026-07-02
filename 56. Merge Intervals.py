
# O(nlogn) Time | O(n) Space
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result=[]
        intervals.sort(key= lambda x:x[0])
        currentinterval = intervals[0]
        result.append(currentinterval)
        for interval in intervals[1:]:
            currentbegin= currentinterval[0]
            currentend = currentinterval[1]
            nextbegin = interval[0]
            nextend = interval[1]
            if currentend >= nextbegin:
                currentinterval[1] = max(currentend,nextend)
            else:
                currentinterval = interval
                result.append(currentinterval)
            
        
                    
        return result
        
        
# O(n^2) Time | O(n) Space (Time limit exceeded output!)

import collections
class Solution:
    def buildGraph(self,array):
        graph = collections.defaultdict(list)
        for i,interval_i in enumerate(array):
            for j in range(i+1,len(array)):
                if self.overlap(interval_i,array[j]):
                    # python dictionary cannot have a list as a key because list is mutable.
                    graph[tuple(interval_i)].append(array[j])
                    graph[tuple(array[j])].append(interval_i)
        return graph
                    
    def getComponents(self,graph,array):
        visited=set()
        component_number =0
        component_graph = collections.defaultdict(list)
        
        def graphdfs(interval):
            stack =[interval]
            while stack:
                node = tuple(stack.pop())
                if node not in visited:
                    visited.add(node)
                    component_graph[component_number].append(node)
                    stack.extend(graph[node])
            return component_graph

        for interval in array:
            if tuple(interval) not in visited:
                graphdfs(interval)
                component_number+=1
        return component_graph,component_number
                
    def overlap(self,array1,array2):
        return array1[0] <= array2[1] and array1[1] >= array2[0]

    def mergeIntervals(self,component_graph,component_number):
        result =[]
        for i in range(component_number):
            min_interval = min(nodes[0] for nodes in component_graph[i])
            max_interval = max(nodes[1] for nodes in component_graph[i])
            result.append([min_interval,max_interval])
        return result
        
    def merge(self,array):
        graph= self.buildGraph(array)
        component_graph, component_number = self.getComponents(graph,array)
        resultFinal =  self.mergeIntervals(component_graph,component_number) 
        return resultFinal
        
object = Solution()
print(object.merge([[1,3],[2,6],[8,10],[15,18]]))

