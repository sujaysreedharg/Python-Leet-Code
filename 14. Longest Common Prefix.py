class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if strs[0]=="":
            return ""
        lcp="".join(["x" for _ in range(200)])
        for i in range(len(strs)-1):
            newlcp=""
            for x in range(len(min(strs[i],strs[i+1]))):
                if strs[i][x]==strs[i+1][x]:
                    newlcp+=strs[i][x]
                else:
                    break
            if len(lcp) > len(newlcp):
                lcp=newlcp
                    
            
        return lcp
