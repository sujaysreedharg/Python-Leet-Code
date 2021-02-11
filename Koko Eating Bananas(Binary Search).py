class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        high = max(piles)
        while low<=high:
            mid  = (low + high)//2
            if (self.possible(piles,mid,H)):
                high = mid -1 
            else:
                low = mid + 1
        return low
    def possible(self, piles,mid,H):
        totalhours = 0 
        for pile in piles:
            div = pile // mid 
            totalhours += div
            if (pile % mid ) !=0:
                totalhours+=1
        return totalhours<=H
