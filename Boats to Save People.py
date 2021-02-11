class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i =0
        j= len(people)-1
        boats=0
        while i<=j:
            boats+=1
            if people[i] + people[j] <=limit:
                i+=1
            j-=1
        return boats
        
       
Time Complexity:O(NlogN), where N is the length of people.

Space Complexity: O(N).
