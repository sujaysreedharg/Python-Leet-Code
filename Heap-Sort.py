def heapSort(array):
    buildMaxHeap(array)
    for endIdx in reversed(range(1,len(array))):
        swap(array,0,endIdx)
        siftdown(array,0,endIdx-1)
    return array


def buildMaxHeap(array):
    firstparent = (len(array)-1)//2
    for currentIdx in reversed(range(firstparent+1)):
        siftdown(array, currentIdx,len(array)-1)
    

def siftdown(heap, currentIdx, endIdx):
    childoneIdx = currentIdx *2 +1
    while childoneIdx<=endIdx:
        childtwoIdx = currentIdx*2+2 if currentIdx*2+2 <=endIdx else -1
        if childtwoIdx>-1 and  heap[childoneIdx] > heap[childtwoIdx]:
            indextoSwap = childtwoIdx
        else:
            indextoSwap = childoneIdx
        if heap[indextoSwap] > heap[currentIdx]:
            swap(heap,indextoSwap,currentIdx)
            currentIdx = indextoSwap
            childoneIdx = currentIdx *2 +1            
        else:
            return
def swap(array,i,j):
    array[i],array[j] = array[j],array[i]
print(heapSort([9,8,7,6,5,4,3,2,1]))
