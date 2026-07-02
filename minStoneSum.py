class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles2=[-i for i in piles]
        
        heapq.heapify(piles2)
        while k>0:
            max_val = -heapq.heappop(piles2)
            max_val-=(max_val//2)
            heapq.heappush(piles2,-max_val)
            k-=1
        return -sum(piles2)
