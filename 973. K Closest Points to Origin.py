class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hashmap=defaultdict(list)
        res=[]
        kpoints=[]
        for point in points:
            dist= ((point[0]-0)**2 +(point[1]-0)**2)**(1/2)
            hashmap[dist].append(point)
            kpoints.append(dist)
        
        kpoints.sort()
        i=0
        while i<k:
            if len(hashmap[kpoints[i]])>0:
                res.extend(hashmap[kpoints[i]])
                i+=len(hashmap[kpoints[i]])
            else:
                res.append(hashmap[kpoints[i]])
                i+=1
                
            
        
        return res
