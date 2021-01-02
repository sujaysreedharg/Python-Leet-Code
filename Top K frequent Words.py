import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap={}
        heap=[]
        for word in words:
            if word not in hashmap:
                hashmap[word]=1
            elif word in hashmap:
                hashmap[word]+=1
        result=[]  
        for word,count in hashmap.items():
                heapq.heappush(heap,[-count,word])
        for i in range(k):
            result.append(heapq.heappop(heap))
        return [word for count,word in result]
        
        
Time: O(n*logk)
Space: O(n)

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
