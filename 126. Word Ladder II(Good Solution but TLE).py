class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        adj_graph=collections.defaultdict(list)
        wordList.append(beginWord)
        for words in wordList:
            for i in range(len(words)):
                pattern = words[:i]+"*"+words[i+1:]
                adj_graph[pattern].append(words)
        q=deque([beginWord])
        visited_level=collections.defaultdict(int)
        visited_level[beginWord]=1
        final_tree =collections.defaultdict(list)
        while q:
            for i in range(len(q)):
                word=q.popleft()
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for child in adj_graph[pattern]:
                        if child not in visited_level:
                            visited_level[child]=visited_level[word]+1
                            q.append(child)
                            final_tree[word].append(child)
                        elif visited_level[child] == visited_level[word]+1:
                            final_tree[word].append(child)
        stack=[]
        ans=[]
        def dfs(beginWord, path,final_tree,ans,endWord):
            path.append(beginWord)
            # print(path)
            if beginWord==endWord:
                ans.append(path.copy())
                # print(ans)
                path.pop()
                return
            for parents in final_tree[beginWord]:
                dfs(parents,path,final_tree,ans,endWord)
            path.pop()
            
            
        dfs(beginWord,stack,final_tree,ans,endWord)
        return ans

            
