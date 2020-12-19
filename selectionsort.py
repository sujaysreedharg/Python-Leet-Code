def selectionsort(array):
  currentindex =0 
  while currentindex < len(array)-1:
    smallestindex= currentindex
    for i in range(currentindex+1,len(array)):
      if array[i]< array[smallestindex]:
        smallestindex=i
    swap(currentindex,smallestindex,array)
    currentindex+=1
  return array
def swap(i,j,array):
  array[i],array[j] = array[j],array[i]
print(selectionsort([10,8,7,64,4]))


O(n^2) Time | O(1) Space
