def mergesort(array):
  if len(array)==1:
    return array
  mididx = len(array)//2
  lefthalf = array[:mididx]
  righthalf = array[mididx:]
  return mergesortedarray(mergesort(lefthalf),mergesort(righthalf))
def mergesortedarray(lefthalf,righthalf):
  sortedarray = [None]* ( len(lefthalf) + len(righthalf))
  i=j=k=0
  while i < len(lefthalf) and j< len(righthalf):
    if lefthalf[i] <= righthalf[j]:
      sortedarray[k] = lefthalf[i]
      i+=1
    else:
      sortedarray[k]= righthalf[j]
      j+=1
    k+=1
  while i < len(lefthalf):
    sortedarray[k]= lefthalf[i]
    i+=1
    k+=1
  while j < len(righthalf):
    sortedarray[k] = righthalf[j]
    j+=1
    k+=1
  return sortedarray

print(mergesort([5,4,2,8,1,7]))

O(nlog(n)) -> Time 
O(nlog(n)) -> Space
