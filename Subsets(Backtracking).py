class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i==len(nums):
                res.append(subset.copy())
                print("res",res)
                return
            subset.append(nums[i])
            print(subset,i)
            dfs(i+1)
            
            subset.pop()
            print("subset after pop",subset,i)
            dfs(i+1)
            print('returned')
            # print("next dfs call", subset)
        dfs(0)   
        return res
        
