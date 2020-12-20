def moveelementtoend(array,element):
  firstptr =0
  endptr = len(array)-1
  while firstptr < endptr:
    while firstptr < endptr and array[endptr]==element:
      endptr-=1
    if array[firstptr] == element:
      array[firstptr],array[endptr] = array[endptr],array[firstptr]
    firstptr+=1
  return array
print(moveelementtoend([1,2,3,4,2,2,2,2],2))



#Doesnt change the order of the elements:
def moveelementtoend(nums,element):
  lastnonzeroat=-1    

  for i in range(0,len(nums)):
    if nums[i] !=element:
      lastnonzeroat+=1
      nums[lastnonzeroat],nums[i]=nums[i], nums[lastnonzeroat] 
  return nums
print(moveelementtoend([1,2,3,4,2,2,2,2],2))

O(n) -> Time
O(1) -> Space
