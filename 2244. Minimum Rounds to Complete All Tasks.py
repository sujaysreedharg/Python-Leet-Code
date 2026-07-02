class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hashmp={}
        res=0
        for i in range(len(tasks)):
            hashmp[tasks[i]]= 1 + hashmp.get(tasks[i],0)
        for keys,values in hashmp.items():
            if values < 2:
                return -1
            else:
                if values%3==0:
                    res+=values//3
                elif values%3!=0:
                    while values%3!=0:
                        res+=1
                        values-=2
                    res+=values//3
        return res
                
            
