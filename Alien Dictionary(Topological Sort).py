from collections import deque
class Sol:
    def aliendictionary(self,words):
        indegree ={}
        graph={}
        for word in words:
            for ch in word:
                indegree[ch]=0
                graph[ch]=[]
        
        for i in range(0,len(words)-1):
            w1,w2 = words[i],words[i+1]
            print(w1,w2)
            for j in range(0,min(len(w1),len(w2))):
                parent,child = w1[j],w2[j]
                if parent!=child:
                    graph[parent].append(child)
                    indegree[child]+=1
                    break
        print(graph,indegree) 
        sources= deque()
        sortedlist =[]
        for key in indegree:
            if indegree[key]==0:
                sources.append(key)
        print(sources) 
        while sources:
            vertex= sources.popleft()
            sortedlist.append(vertex)
            for child in graph[vertex]:
                indegree[child]-=1
                if indegree[child]==0:
                    sources.append(child)
        return sortedlist
        


sol = Sol()
print(sol.aliendictionary(["cab", "aaa", "aab"]))
print(sol.aliendictionary(["ywx", "wz"]))
print(sol.aliendictionary(["ba", "bc", "ac", "cab"]))


Time -> O(V+N)
Space -> O(V+N)


Output: 
cab aaa
aaa aab
{'c': ['a'], 'a': ['b'], 'b': []} {'c': 0, 'a': 1, 'b': 1}
deque(['c'])
['c', 'a', 'b']
ywx wz
{'y': ['w'], 'w': [], 'x': [], 'z': []} {'y': 0, 'w': 1, 'x': 0, 'z': 0}
deque(['y', 'x', 'z'])
['y', 'x', 'z', 'w']
ba bc
bc ac
ac cab
{'b': ['a'], 'a': ['c', 'c'], 'c': []} {'b': 0, 'a': 1, 'c': 2}
deque(['b'])
['b', 'a', 'c']
