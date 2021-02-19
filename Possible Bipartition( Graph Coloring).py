class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        notcolored,red,green = 0,1,-1
        

        def helper(person_id,color):
            colortable[person_id]=color
            for other_persons in dislikestable[person_id]:
                if colortable[other_persons]==color:
                    return False
                if colortable[other_persons]==notcolored and (not helper(other_persons,-color)):
                    return False

            return True
        if  N==1 or not dislikes:
            return True
        colortable = [ notcolored for _ in range(N+1)]
        dislikestable = collections.defaultdict(list)
        for p1,p2 in dislikes:
            dislikestable[p1].append(p2)
            dislikestable[p2].append(p1)
        for person_id in range(1,N+1):
            if colortable[person_id]==notcolored and (not helper(person_id,red)):
                return False
        return True
            
            
        
                
