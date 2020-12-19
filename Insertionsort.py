def insertionsort(array):
  for i in range(0,len(array)):
    j=i
    while j>0 and array[j]<array[j-1]:
      swap(j,j-1,array)
    
  return array
def swap(i,j,array):
  array[i],array[j] = array[j],array[i]
print(insertionsort([10,8,7,64,4]))





Space Complexity = O(1)
Time Complexity = O(n^2)
