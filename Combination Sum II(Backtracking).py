class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result =set()
        candidates.sort()
        self.backtrack(candidates,target,0,[],result)
        return list(result)
    def backtrack(self,candidates,target,startidx,currlist,result):
        if target==0:
            result.add(tuple(currlist[:]))
            return
        if target<0:
            return
        for i in range(startidx,len(candidates)):
            if i>0 and candidates[i]==candidates[i-1] and i!=startidx:    
                continue
            currlist.append(candidates[i])
            self.backtrack(candidates,target-candidates[i],i+1,currlist,result)
            currlist.pop()
