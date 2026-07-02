class Solution:
    def verticalTraversal(self, root):
        dic=defaultdict(list)
        self.min_h,self.max_h=float("inf"),-float("inf")
        out=[]
        def dfs(root,level_h,level_v):
            self.min_h=min(level_h,self.min_h)
            self.max_h=max(level_h,self.max_h)
            dic[level_h].append((level_v,root.val))
            if root.left: dfs(root.left,level_h-1,level_v+1)
            if root.right: dfs(root.right,level_h+1,level_v+1)
        dfs(root,0,0)       
        for i in range(self.min_h,self.max_h+1):
            out+=[[j for x,j in sorted(dic[i])]]
        return out
