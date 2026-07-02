# O(n) Time | O(n) Space

def twoSum(array,target):
    hashmap={}
    for num in array:
        potentialMatch = target - num
        if potentialMatch in hashmap:
            return [potentialMatch,num]
        else:
            hashmap[num]= True

print(twoSum([3,5,-4,8,11,1,-1,6],10))


# O(nlogn) Time | O(1) Space

def twoSum(array,target):
    array.sort()
    i=0
    j=len(array)-1
    while i<j:
        result = array[i] + array[j]
        if result == target:
            return [array[i],array[j]]
        elif result < target:
            i+=1
        else:
            j-=1
    return False 
        

print(twoSum([3,5,-4,8,11,1,-1,6],8))
