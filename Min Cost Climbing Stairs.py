class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1,step2=0,0
        for x in reversed(cost):
            currentstep= x+ min(step1,step2)
            step1=step2
            step2 = currentstep
            print("currentstep")
            print(currentstep)
            print('step1')
            print(step1)
            print('step2')
            print(step2)
        return min(step1,step2)
        
        Time -> O(n)
        Space -> O(1)
