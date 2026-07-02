# O(n^2) Time |  O(1) Space
def insertionSort(array):
    for i in range(1,len(array)):
        j=i
        while(j>0) and array[j] < array[j-1]:
            #swap em
            array[j],array[j-1] = array[j-1],array[j]
            j-=1
    return array        
print(insertionSort([7,6,5,4,3,2,1]))
