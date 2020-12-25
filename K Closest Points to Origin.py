class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        distances= list(map(self.negativedistancecalc,points))
        maxheap = distances[:K]
        heapq.heapify(maxheap)
        for items in distances[K:]:
            heapq.heappushpop(maxheap,items)
        return list(map(lambda x: x[1], maxheap))
        
    def negativedistancecalc(self,points):
        x,y = points
        return (-(x**2 + y**2),points)
        
        
        
def negative_distance( point):
  x,y = point
  return (-((x**2 + y**2)), point)
import heapq


distances = list(map(negative_distance, [[3,3],[5,-1],[-2,4]]))
maxheap = distances[:2]
heapq.heapify(maxheap)
for d in distances[2:]:
  heapq.heappushpop(maxheap, d)
print(list(map(lambda x: x[1], maxheap))) 
print(maxheap)
print(distances)



O(k + (n-k) logk) -> Time
O(n) -> Space (idk)



Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

