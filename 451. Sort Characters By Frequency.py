class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap={}
        for string in s:
            if string not in hashmap:
                hashmap[string]=1
            else:
                hashmap[string]+=1
        
        lists=[[k,hashmap[k]] for k in hashmap]
        lists.sort(key= lambda x: x[1])

        result=[]
        for i in reversed(range(len(lists))):

            while lists[i][1]>0:
                result.append(lists[i][0])
                lists[i][1]-=1
        return ''.join(result)
                
            
