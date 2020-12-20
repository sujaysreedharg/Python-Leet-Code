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



O(n) -> Time
O(1) -> Space
