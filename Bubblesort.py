def bubblesort(array):
  issorted =False
  while not issorted :
    issorted =True
    counter = 0
    for i in range(0,len(array)-1-counter):
      if (array[i] > array[i+1]):
        swap(i,i+1,array)
        issorted=False
        counter+=1
    
  return array
def swap(i,j,array):
  array[i],array[j] = array[j],array[i]
print(bubblesort([10,8,7,64,4]))

# Time complexity : O(n^2) Worst and average cases,while in the best case where the array is already sorted the time complexity would be O(n)
#Space complexity :  O(1) because in-place and there is no storage using a helping array or something
  
