def quicksort(array):
  quicksorthelper(array,0,len(array)-1)
  return array
def quicksorthelper(array, startidx,endidx):
  if startidx>=endidx:
    return 
  pivotidx = startidx
  leftidx =startidx+1
  rightidx = endidx
  while rightidx >= leftidx:
    if array[leftidx]> array[pivotidx] and array[rightidx]< array[pivotidx]:
      swap(leftidx,rightidx,array)
    elif array[leftidx] < array[pivotidx]:
      leftidx+=1
    elif array[rightidx] > array[pivotidx]:
      rightidx-=1
  swap(pivotidx,rightidx,array)
  leftidxarrayissmaller = rightidx -1 - startidx < endidx - (rightidx+1)
  if leftidxarrayissmaller:
    quicksorthelper(array,startidx, rightidx-1)
    quicksorthelper(array, rightidx+1,endidx)
  else:
    quicksorthelper(array, rightidx+1,endidx)
    quicksorthelper(array,startidx, rightidx-1)
def swap(i,j,array):
  array[i],array[j]=  array[j],array[i]
print(quicksort([5,4,2,8,1,7]))

O(nlog(n)) -> Time (Best and Average)
O(n^2) -> Time (Worst)
O(log(n)) -> Space
