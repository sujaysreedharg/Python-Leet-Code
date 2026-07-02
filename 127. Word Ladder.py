class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        graph= collections.defaultdict(list)
        wordList.append(beginWord)
        for words in wordList:
            for i in range(len(words)):
                pattern = words[:i]+"*"+words[i+1:]
                graph[pattern].append(words)
        res=1
        visited=set(beginWord)
        q=deque([beginWord])
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return res
                for i in range(len(word)):
                    pattern=word[:i]+"*"+ word[i+1:]
                    for neigh in graph[pattern]:

                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)
            res+=1
        return 0
