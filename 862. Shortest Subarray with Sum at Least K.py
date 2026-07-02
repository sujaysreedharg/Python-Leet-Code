class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        dq = collections.deque()
        sums = 0 
        shortest = float("inf")
        curr = (float("inf"), float("inf"))
        for i in range(len(nums)):
            sums += nums[i]
            if sums >=k:
                shortest = min(shortest, i+1)
            
            
            
            while dq and sums - dq[0][0] >= k:
                curr = dq[0]
                dq.popleft()
            
            if curr[1] != float("inf"):
                shortest  = min(shortest, i-curr[1])
            
            while dq and sums <= dq[-1][0]:
                dq.pop()
            dq.append((sums,i))
            
        return shortest if shortest!= float("inf") else -1
            
