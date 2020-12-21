import heapq 
def topKFrequent(nums,k):
  ans=[]
  if k == len(nums):
            
    return nums
  hashmap={}  
  for i in range(0,len(nums)):         
    num=nums[i]
    if num not in hashmap:
      hashmap[num]=1
    else:
      hashmap[num]+=1
  for key,value in hashmap.items():
    if len(ans)<k:
      heapq.heappush(ans,[value,key])
    else:
      heapq.heappushpop(ans,[value,key])
  return [key for value,key in ans]

print(topKFrequent([1,1,1,1,2,2,3,3,3],2))



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
