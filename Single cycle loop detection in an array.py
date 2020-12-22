def circularArrayLoop(nums):
  numelementvisited=0
  currentidx=0
  while numelementvisited<len(nums):
    if numelementvisited > 0 and currentidx==0:
      return False
    numelementvisited+=1
    currentidx = getnextidx(currentidx,nums)
  return currentidx==0
        
def getnextidx(currentidx,nums):
        
  jump=nums[currentidx]
  nextidx = (currentidx+jump) % len(nums)
  return nextidx if nextidx>=0 else  nextidx + len(nums)
print(circularArrayLoop([2,3,1,-4,-4,2]))





O(n) -> Time
O(1) -> Space
