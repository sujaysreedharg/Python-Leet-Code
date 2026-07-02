class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        res=[]
        
        
        
        def backtrack(target, pos,path):
            if target ==0:
                res.append(path[:])
            if target < 0:
                return
            prev=-1
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                path.append(candidates[i])
                backtrack(target-candidates[i], i+1, path)
                path.pop()
                prev= candidates[i]
        backtrack(target, 0, [])
        
        return res
