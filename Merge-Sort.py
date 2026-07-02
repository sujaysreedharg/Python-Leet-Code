#merge sort
# O(nlogn) Time | O(n) Space
arr= [7,6,4,3,1,2]
def mergeSort(arr):
    if len(arr)==1:
        return arr
    mid = len(arr)//2
    lefthalf=mergeSort(arr[:mid])
    righthalf=mergeSort(arr[mid:])
    return mergeArr(lefthalf,righthalf)

def mergeArr(lefthalf,righthalf):
    result = [None]*(len(lefthalf) + len(righthalf))
    i=j=k=0
    while i<len(lefthalf) and j<len(righthalf):
        if lefthalf[i] < righthalf[j]:
            result[k]=lefthalf[i]
            i+=1
            k+=1
        elif lefthalf[i] >righthalf[j]:
            result[k] =righthalf[j]
            j+=1
            k+=1
    while i<len(lefthalf):
        result[k]= lefthalf[i]
        i+=1
        k+=1
    while j<len(righthalf):
        result[k]=righthalf[j]
        j+=1
        k+=1
    return result
        
print(mergeSort(arr))
