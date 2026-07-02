class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes,key=lambda x: x[1],reverse=True)
        units=0
        # print(boxTypes)
        for box in boxTypes:
            for i in range(box[0]):
                units+=box[1]
                truckSize-=1
                if truckSize==0:
                    return units
        return units
            

        
        
        
