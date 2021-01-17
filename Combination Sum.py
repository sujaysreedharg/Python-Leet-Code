class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.backtrack(candidates,target,0,[],result)
        return result
        
    def backtrack(self,candidates,target,startidx,currentcandidates,result):
        if target==0:
            result.append(currentcandidates[:])
            return 
        if target<0:
            return
        
        for i in range(startidx,len(candidates)):
            currentcandidates.append(candidates[i])
            
            self.backtrack(candidates,target-candidates[i],i,currentcandidates,result)
        
            currentcandidates.pop()
